
#!/usr/bin/env python3

"""Main code for CircuitPython."""

# pylint: disable=E0401
import board
import digitalio
import supervisor
import storage

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType

from ergodash.ergodash import Ergodash

def debug_print(*argv):
    """print message to serial consol."""
    if keyboard.debug_enabled:
        print(*argv)


def is_usb_connected():
    """trickly way to check usb sorage and serial is enabled or not."""
    try:
        storage.remount("/", readonly=False)  # attempt to mount readwrite
        storage.remount("/", readonly=True)  # attempt to mount readonly
    except RuntimeError as _:
        return True
    return False



keyboard = KMKKeyboard()
keyboard.debug_enabled = is_usb_connected()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

ergodash = Ergodash(keyboard.debug_enabled)
keyboard.keymap = ergodash.keymap
keyboard.col_pins = ergodash.col_pins
keyboard.row_pins = ergodash.row_pins
data_pin = board.GP0
data_pin2 = board.GP1


split = Split(
    split_side=ergodash.split_side,
    split_flip=False,
    # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=data_pin,
    data_pin2=data_pin2,
    debug_enabled=keyboard.debug_enabled,
    # If you want the right to be the target, change this to false
)

#keyboard.modules.append(split)

if __name__ == "__main__":
    try:
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT
        led.value = True
        keyboard.go()
    except Exception as inst:  # pylint: disable=W0703
        debug_print(inst)
        supervisor.reload()
