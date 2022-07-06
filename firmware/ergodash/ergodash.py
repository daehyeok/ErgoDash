#!/usr/bin/env python3

import board
import digitalio
import storage

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from ergodash.layout import Keymap
from ergodash.pins import Pinconfig

from kmk.modules.split import Split, SplitSide, SplitType

def _usb_mounted():
    """trickly way to check usb sorage and serial is enabled or not."""
    try:
        storage.remount("/", readonly=False)  # attempt to mount readwrite
        storage.remount("/", readonly=True)  # attempt to mount readonly
    except RuntimeError as _:
        return True
    return False

class Ergodash(_KMKKeyboard):

    split_side = SplitSide.LEFT

    debug_enabled = _usb_mounted()
    diode_orientation = DiodeOrientation.COL2ROW
    keymap=Keymap
    coord_mapping = list(range(70))

    _tx_pin=board.GP0
    _rx_pin=board.GP1
    _handress_pin= digitalio.DigitalInOut(board.GP5)

    def log(self,*argv):
        """print message to serial consol."""
        if self.debug_enabled:
            print(*argv)

    def __init__(self, split_side=None):
        if split_side is not None:
            self.split_side = split_side
        else:
            self.split_side = SplitSide.LEFT if self._handress_pin.value else SplitSide.RIGHT

        if(self.split_side == SplitSide.LEFT):
            self.col_pins = Pinconfig.LEFT_COL_PINS
            self.row_pins = Pinconfig.LEFT_ROW_PINS
        else:
            self.col_pins = Pinconfig.RIGHT_COL_PINS
            self.row_pins = Pinconfig.RIGHT_ROW_PINS

        self.is_host = self.split_side == SplitSide.RIGHT
        self._init_split_module()
        self.log(f"Ergodox Init: {self.split_side}")

    def _split_target_left(self):
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
