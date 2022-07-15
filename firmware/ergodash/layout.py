from kmk.keys import KC

_______ = KC.TRNS

# EXAMPLE_TD = KC.TD(
#     # Tap once for "a"
#     KC.A,
#     # Tap twice for "b", or tap and hold for "left control"
#     KC.MT(KC.B, KC.LCTL, prefer_hold=False),
#     # Tap three times to send a raw string via macro
#     send_string('macros in a tap dance? I think yes'),
#     # Tap four times to toggle layer index 1, tap 3 times and hold for 3s to
#     # momentary toggle layer index 1.
#     KC.TT(1, tap_time=3000),
# )

# pylint: disable=C0301
# fmt: off
Keymap = [
    [
        # 0         1         2        3         4       5         6          7        8          9         10       11       12        13
        KC.GESC, KC.N1,    KC.N2,   KC.N3,   KC.N4,    KC.N5,    KC.MINS,  KC.EQL,   KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,  KC.BKDL,
        KC.TAB,   KC.Q,     KC.W,    KC.E,    KC.R,     KC.T,     KC.LBRC,  KC.RBRC,  KC.Y,      KC.U,     KC.I,     KC.O,      KC.P,   KC.BSLS,
        KC.LCTRL, KC.A,     KC.S,    KC.D,    KC.F,     KC.G,     _______,  _______,  KC.H,      KC.J,     KC.K,     KC.L,     KC.SCLN, KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,    KC.V,     KC.B,     _______,  _______,  KC.N,      KC.M,     KC.COMM,  KC.DOT,  KC.SLSH,  KC.RSFT,
        _______,  KC.CAPS, _______,  KC.LALT, KC.LGUI,  KC.SPC,   _______,  _______,  KC.ENT,   KC.BKDL,  KC.LEFT,  KC.UP,   KC.DOWN, KC.RGHT,
    ]
]
# fmt: on
