# Minitel-maton

Inspired by our AsciiMaton, here is the Minitel-maton.

Take a picture, display it on a Minitel (model 1B here) and print it on a good old dot matrix printer (Epson LX-800)!

To print images directly on dot matrix printers (LX-800, for example), use ´to_printer()` function.

## Wiring:

Using a 5v USB-TTL converter, connect it to the minitel following this:
https://pila.fr/wordpress/?p=361 (source in french)

## Usage:
Power-up the Raspberry Pi and the printer, run `minimaton.py` and enjoy!

Communication being done via a serial-to-usb converter, weird stuff and interferences can happen. Try to reboot the pi, plug/unplug the adapter etc. Be sure to have everything "ready" before trying to print (don't connect the printer after running the script, for example).

Written in python3 for Raspberry Pi 3.

Black and white dithering is a bit slow (takes up to 15sec to dither) on Pi3


## Thanks to:
* Pankaj
* Neodyme
* Tecknoplay
* Ramiro

## Sources:
* PyMinitel lib: https://github.com/Zigazou/PyMinitel

## Disclaimer
I'm not a python programmer... Neither a real programmer. I'm mastering copy/pasting...