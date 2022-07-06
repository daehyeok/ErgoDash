
#!/usr/bin/env python3

"""Main code for CircuitPython."""

# pylint: disable=E0401
import board
import digitalio
import supervisor

from kmk.modules.split import SplitSide

from ergodash.ergodash import Ergodash

ergodash = Ergodash()

if __name__ == "__main__":
    try:
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT
        led.value = True
        ergodash.go()
    except Exception as inst:  # pylint: disable=W0703
        ergodash.log(inst)
        supervisor.reload()
