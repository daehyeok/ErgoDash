PICO_PATH=/Volumes/CIRCUITPY

.DEFAULT_GOAL := code

CMD=rsync
CMD_ARGS=-r

kmk: kmk_firmware
	$(CMD) $(CMD_ARGS) kmk_firmware/kmk $(PICO_PATH)

neopixel: lib
	$(CMD) $(CMD_ARGS) lib $(PICO_PATH)

boot: boot.py
	$(CMD) $(CMD_ARGS) boot.py $(PICO_PATH)/boot.py

code: code.py
	$(CMD) $(CMD_ARGS) code.py $(PICO_PATH)/code.py

all: kmk neopixel boot code
