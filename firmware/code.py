
#!/usr/bin/env python3

"""Main code for CircuitPython."""

# pylint: disable=E0401
import supervisor

from ergodash.ergodash import Ergodash

ergodash = Ergodash()

if __name__ == "__main__":
    try:
        ergodash.go()
    except Exception as inst:  # pylint: disable=W0703
        ergodash.log(inst)
        supervisor.reload()
