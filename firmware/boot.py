#!/usr/bin/env python3

"""Runs only once on start up before USB is initialized."""

# pylint: disable=E0401
import board
import digitalio
import storage
import usb_midi
import usb_cdc


def is_right():
    handress_pin = digitalio.DigitalInOut(board.GP27)
    value = handress_pin.value
    handress_pin.deinit()
    return value

def is_dev():
    """Consider it is dev mode, If spacebar is pressed during boot up."""
    handress_pin = digitalio.DigitalInOut(board.GP5)
    is_left = not handress_pin.value
    handress_pin.deinit()

    dev_mode = False
    space_col_pin = digitalio.DigitalInOut(board.GP11)
    space_row_pin = digitalio.DigitalInOut(board.GP15)

    if not is_right():
        space_col_pin = digitalio.DigitalInOut(board.GP9)
        space_row_pin = digitalio.DigitalInOut(board.GP5)

    space_col_pin.direction = digitalio.Direction.OUTPUT
    space_row_pin.switch_to_input(pull=digitalio.Pull.DOWN)

    space_col_pin.value = True
    dev_mode = space_row_pin.value

    space_col_pin.value = False
    space_col_pin.deinit()
    space_row_pin.deinit()

    return dev_mode

if not is_dev():
    usb_cdc.disable()
    storage.disable_usb_drive()
    usb_midi.disable()
