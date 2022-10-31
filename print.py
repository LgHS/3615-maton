#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import cv2
import numpy as np
import time
from datetime import datetime

from minitel.Minitel import Minitel
from minitel.ImageMinitel import ImageMinitel
from PIL import Image
from time import sleep
import signal
import sys
import requests

from decouple import config

LGHS_KIKK_BEARER = config('LGHS_KIKK_BEARER')
TXT_FOOTER_1 = config('TXT_FOOTER_1')
TXT_FOOTER_2 = config('TXT_FOOTER_2')


print_width = 320
print_height = int((240/320)*print_width)
w_fs = "y" # With or without FS?

def to_printer():
    print("printing...")
    img = cv2.imread("resources/print.jpg")
    try:
        with  open('/dev/usb/lp0', "wb") as printer:
            try:
                printer.write(bytearray(b"\x1b\x40")) ## ESC @ // initialise printer

                img = Image.fromarray(img) # From opencv Array to PIL Image

                img_w, img_h = img.size
                wh = img_w>>8
                wl = img_w & 255

                for i in range (0,5):
                    printer.write(bytearray(b"\x1b\x33\x18")) ## ESC 3 24 // line spacing

                #printer.write(bytearray(b"\x1b\x50")) ## ESC P // 10CPI
                #printer.write(bytearray(b"\x1b\x6c\x12")) ## ESC l 10 // 1 inch left margin

                for i in range (0,20):
                    printer.write(bytearray(b"\x0a\x0d")) ## \n\r

                for y in range(0, img_h-8, 8):
                    printer.write(bytearray(b"\x0a\x0d")) ## \n\r
                    printer.write(bytearray(b"\x1b\x33\x18")) ## ESC 3 24 // reset line spacing each line, just to be sure
                    printer.write(bytearray(b"\x1b\x2a\x05")) ## ESC * 5 wl wh // Bit image graphics mode
                    printer.write(wl.to_bytes(1, 'little'))
                    printer.write(wh.to_bytes(1, 'little'))
                    print(y)
                    for x in range(0, img_w):
                        b=0
                        if (img.getpixel((x, y)) == 0): b = b | 128
                        if (img.getpixel((x, y+1)) == 0): b = b | 64
                        if (img.getpixel((x, y+2)) == 0): b = b | 32
                        if (img.getpixel((x, y+3)) == 0): b = b | 16
                        if (img.getpixel((x, y+4)) == 0): b = b | 8
                        if (img.getpixel((x, y+5)) == 0): b = b | 4
                        if (img.getpixel((x, y+6)) == 0): b = b | 2
                        if (img.getpixel((x, y+7)) == 0): b = b | 1
                        printer.write(b.to_bytes(1, 'little'))

                for i in range (0,53):
                    printer.write(bytearray(b"\x0a\x0d")) ## \n\r

            except OSError as e:
                print('Error when printing')
                minitel.position(4,22)
                minitel.envoyer('Error when printing...                               ')
                print(e)
                
    except FileNotFoundError as e:
        print('ERROR!\nCan\'t seem to contact printer')

    printer.close()

    print("Ready")

    return True
