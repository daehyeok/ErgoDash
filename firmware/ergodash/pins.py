#!/usr/bin/env python3

import board

class Pinconfig:
    LEFT_ROW_PINS=[
                board.GP20,
                board.GP21,
                board.GP27,
                board.GP22,
                board.GP26,
            ]

    LEFT_COL_PINS =  [board.GP9,
                board.GP8,
                board.GP7,
                board.GP16,
                board.GP17,
                board.GP18,
                board.GP19,
                ]


    RIGHT_ROW_PINS= [
                board.GP16,
                board.GP7,
                board.GP27,
                board.GP8,
                board.GP9]

    RIGHT_COL_PINS = [ board.GP17,
                   board.GP18,
                   board.GP19,
                   board.GP20,
                   board.GP21,
                   board.GP22,
                   board.GP26,
                  ]
