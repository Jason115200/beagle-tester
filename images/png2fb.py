#!/usr/bin/env python

# http://stackoverflow.com/questions/19131556/how-to-get-rgb888-24-bit-and-rgb565-16-bit-framebuffer-dump-from-a-jpg-ima

import sys
from PIL import Image

if len(sys.argv) > 2:
    # print "\nReading: " + sys.argv[1]
    out = open(sys.argv[2], "wb")
elif len(sys.argv) == 2:
    out = sys.stdout
else:
    print "Usage: png2fb.py infile [outfile [-32]]"
    sys.exit(1)

im = Image.open(sys.argv[1])
mode = sys.argv[2]

if im.mode == "RGB":
    pixelSize = 3
elif im.mode == "RGBA":
    pixelSize = 4
else:
    sys.exit('not supported pixel mode: "%s"' % (im.mode))

pixels = im.tobytes()
if mode == "-32":
    pixels2 = ""
    for i in range(0, len(pixels) - 1, pixelSize):
        pixels2 += chr(ord(pixels[i]))
        pixels2 += chr(ord(pixels[i + 1]))
        pixels2 += chr(ord(pixels[i + 2]))
    out.write(pixels2)
else:
    pixels2 = ""
    for i in range(0, len(pixels) - 1, pixelSize):
        pixels2 += chr(ord(pixels[i + 2]) >> 3 | (ord(pixels[i + 1]) << 3 & 0xe0))
        pixels2 += chr(ord(pixels[i]) & 0xf8 | (ord(pixels[i + 1]) >> 5 & 0x07))
    out.write(pixels2)
out.close()
