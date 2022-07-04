#!/usr/bin/env python3

"""Runs only once on start up before USB is initialized."""

# pylint: disable=E0401
import board
import digitalio
import storage
import usb_midi
import usb_cdc


def is_dev():
    """Consider it is dev mode, If spacebar is pressed during boot up."""
    vbus_detect_pin = digitalio.DigitalInOut(board.GP24)
    vbus_detected = vbus_detect_pin.value
    vbus_detect_pin.deinit()

    if not vbus_detected:
        return False

    handress_pin = digitalio.DigitalInOut(board.GP5)
    is_left = not handress_pin.value
    handress_pin.deinit()

    dev_mode = False
    if is_left:
        space_col_pin = digitalio.DigitalInOut(board.GP2)
        space_row_pin = digitalio.DigitalInOut(board.GP8)
        space_col_pin.direction = digitalio.Direction.OUTPUT
        space_row_pin.switch_to_input(pull=digitalio.Pull.DOWN)

        space_col_pin.value = True
        dev_mode = space_row_pin.value

        space_col_pin.value = False
        space_col_pin.deinit()
        space_row_pin.deinit()
    else:
        dev_mode = vbus_detected

    return dev_mode


if not is_dev():
    usb_cdc.disable()
    storage.disable_usb_drive()
    usb_midi.disable()
