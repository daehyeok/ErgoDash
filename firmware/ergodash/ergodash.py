#!/usr/bin/env python3

import board
import digitalio
import storage
import neopixel

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

# from ergodash.layout import Keymap
from ergodash.pins import Pinconfig

from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.oneshot import OneShot
from kmk.modules.layers import Layers


extra_modules=[
    Layers(),
    OneShot(),
    TapDance()]

launcher = simple_key_sequence(
    (KC.OS(KC.LGUI, tap_time=None),  KC.SPC)
)


_______ = KC.TRNS
esc_td = KC.TD(
    KC.GRV,
    KC.ESC
)

Keymap = [
    [
        # 0         1         2        3         4       5         6          7        8          9         10       11       12        13
        KC.GRV,   KC.N1,    KC.N2,   KC.N3,   KC.N4,    KC.N5,    KC.MINS,   KC.EQL,   KC.N6,    KC.N7,    KC.N8,    KC.N9,   KC.N0,   KC.BKDL,
        KC.TAB,   KC.Q,     KC.W,    KC.E,    KC.R,     KC.T,     KC.LBRC,   KC.RBRC,  KC.Y,     KC.U,     KC.I,     KC.O,    KC.P,    KC.BSLS,
        KC.LCTRL, KC.A,     KC.S,    KC.D,    KC.F,     KC.G,     _______,   _______,  KC.H,     KC.J,     KC.K,     KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,    KC.V,     KC.B,     KC.ESC,  _______,  KC.N,     KC.M,     KC.COMM,  KC.DOT,  KC.SLSH, KC.RSFT,
        _______,  KC.CAPS,  _______, KC.LALT, KC.LGUI,  KC.SPC,   KC.MO(1),  KC.BKDL,  KC.SPC,   KC.ENT,   KC.LEFT,  KC.UP,   KC.DOWN, KC.RGHT,
    ],
    [
        # 0         1         2        3         4       5         6          7        8          9         10       11       12        13
        _______,   KC.N1,    KC.N2,   KC.N3,   KC.N4,    KC.N5,   _______,   _______,  KC.N6,    KC.N7,    KC.N8,    KC.N9,   KC.N0,   KC.BKDL,
        _______,  _______,  _______,  _______, _______,  _______, _______,   _______,  _______,  _______,  KC.MINS,  KC.EQL, _______, _______,
        _______,  _______,  _______,  _______, _______,  _______, _______,   _______,  _______,  _______,  KC.LBRC,  KC.RBRC,  _______, _______,
        _______,  _______,  _______,  _______, _______,  _______, _______,   _______,  _______,  _______,  _______,  _______, _______, _______,
        _______,  _______,  _______,  _______, _______,  _______, _______,   _______,  _______,  _______,  _______,  _______, _______, _______,

    ]
]

def _usb_mounted():
    """trickly way to check usb sorage and serial is enabled or not."""
    try:
        storage.remount("/", readonly=False)  # attempt to mount readwrite
        storage.remount("/", readonly=True)  # attempt to mount readonly
    except RuntimeError as _:
        return True
    return False

def IsRight():
    handress_pin = digitalio.DigitalInOut(board.GP27)
    value = handress_pin.value
    handress_pin.deinit()

class Ergodash(_KMKKeyboard):

    split_side = SplitSide.LEFT

    debug_enabled = _usb_mounted()
    diode_orientation = DiodeOrientation.COL2ROW
    keymap=Keymap

    _tx_pin=board.GP0
    _rx_pin=board.GP1
    _handress_pin= digitalio.DigitalInOut(board.GP27)
    _pixel_pin = board.GP17

    def log(self,*argv):
        """print message to serial consol."""
        if self.debug_enabled:
            print(*argv)

    def __init__(self, split_side=None):
        if split_side is not None:
            self.split_side = split_side
        else:
            self.split_side = SplitSide.RIGHT if self._handress_pin.value else SplitSide.LEFT

        if(self.split_side == SplitSide.LEFT):
            self.col_pins = Pinconfig.LEFT_COL_PINS
            self.row_pins = Pinconfig.LEFT_ROW_PINS
        else:
            self.col_pins = Pinconfig.RIGHT_COL_PINS
            self.row_pins = Pinconfig.RIGHT_ROW_PINS

        self.pixel = neopixel.NeoPixel(self._pixel_pin, 1, brightness=0.3)

        self.modules.extend(extra_modules)
        self.is_host = self.split_side == SplitSide.RIGHT
        self._init_split_module()
        self.log(f"Ergodox Init: {self.split_side}")

    def _split_target_left(self):
        return False
        if self.split_side == SplitSide.LEFT:
            return self.is_host

        return not self.is_host

    def _init_split_module(self):
        data_pin, data_pin2 = self._tx_pin, self._rx_pin
        if(self.is_host):
            data_pin, data_pin2 = self._rx_pin, self._tx_pin

        split = Split(
            split_side=self.split_side,
            split_flip=False,
            # Sets if this is to
            split_target_left=self._split_target_left(),
            split_type=SplitType.UART,# Defaults to
            data_pin=data_pin,
            data_pin2=data_pin2,
            debug_enabled=self.debug_enabled,
            # If you want the right to be the target, change this to false
        )
        self.modules.append(split)
