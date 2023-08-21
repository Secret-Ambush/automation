#!/usr/bin/env python3

from PIL import Image
from glob import glob
import os

# Specify the path to the image directory
image_directory = 'image/'

# Iterate through each file in the image directory
for file in glob(os.path.join(image_directory, 'ic_*')):
    print("Processing:", file)  # Debugging line
    image = Image.open(file).convert('RGB')

    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]  # get filename without extension

    # Debugging line
    print("Before processing:", image.format, image.size, image.mode)

    rotated_resized_image = image.rotate(270).resize((
