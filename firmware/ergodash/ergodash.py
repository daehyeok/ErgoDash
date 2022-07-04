#!/usr/bin/env python3

import board
import digitalio
from ergodash.layout import Keymap
from ergodash.pins import Pinconfig

from kmk.modules.split import SplitSide

class Ergodash:

    split_side = SplitSide.LEFT
    handress_pin= digitalio.DigitalInOut(board.GP5)
    debug_enabled = False

    def _log(self,*argv):
        """print message to serial consol."""
        if self.debug_enabled:
            print(*argv)

    def __init__(self,debug_enabled=False, split_side=None):
        self.debug_enabled = debug_enabled
        self.keymap=Keymap

        if split_side is not None:
            self.split_side = split_side
        else:
            self.split_side = SplitSide.LEFT if self.handress_pin.value else SplitSide.RIGHT

        if(self.split_side == SplitSide.LEFT):
            self.col_pins = Pinconfig.LEFT_COL_PINS
            self.row_pins = Pinconfig.LEFT_ROW_PINS
        else:
            self.col_pins = Pinconfig.RIGHT_COL_PINS
            self.row_pins = Pinconfig.RIGHT_ROW_PINS

        self._log(f"Ergodox Init: {self.split_side}")
