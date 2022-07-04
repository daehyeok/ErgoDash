#!/usr/bin/env python3

from kmk.keys import KC

_______ = KC.TRNS

# pylint: disable=C0301
# fmt: off
Keymap = [
    [
        # 0         1         2        3         4       5         6          7        8          9         10       11       12        13
        KC.GRAVE, KC.N1,    KC.N2,   KC.N3,   KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,   KC.N9,    KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,    KC.E,    KC.R,     KC.T,     KC.Y,     KC.Y,     KC.U,    KC.I,     KC.O,    KC.P,    KC.LBRC, KC.RBRC,
        KC.LCTRL, KC.A,     KC.S,    KC.D,    KC.F,     KC.G,     _______,  KC.H,     KC.J,    KC.K,     KC.L,    KC.SCLN, KC.QUOT, _______,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,    KC.V,     KC.B,     _______,  KC.B,     KC.N,    KC.M,     KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
        _______,  KC.CAPS,  KC.LALT, KC.LGUI, KC.SPC,  _______,  _______,  _______,   KC.RGUI, KC.SPC,   KC.RGUI, KC.RALT, _______, KC.LEFT,
    ]
]
# fmt: on
