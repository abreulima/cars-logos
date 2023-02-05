from PIL import Image
import cv2
import numpy as np
import os


base = "logo-max-resolution"
output = "black-and-white"
files = os.listdir(base)

for f in files:


    ext = f.split(".")

    if ext[1] != "png":
        continue

    print(f)
    im = Image.open(os.path.join(base, f))

    if im.mode != "RGBA":
        im = im.convert("RGBA")

    # Create a new image to hold the result
    result = Image.new("RGBA", im.size, (0, 0, 0, 0))

    # Loop through each pixel in the original image
    for x in range(im.width):
        for y in range(im.height):
            # If the pixel is not transparent, set it to black
            if im.getpixel((x, y))[3] != 0:
                result.putpixel((x, y), (0, 0, 0, 255))


    result.save(os.path.join(output,f))
