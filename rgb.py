from PIL import Image
import numpy as np
import os

rgb_input = input("format (example, '70,130,180'): ")
rgb_value = tuple(map(int, rgb_input.split(',')))

width, height = 1920, 1080

image = Image.fromarray(np.full((height, width, 3), rgb_value, dtype=np.uint8))
file_name = input("Input file name")

image_path = "/home/tarik"
exact_path = os.path.join(image_path, file_name)
image.save(exact_path)

print(f"Saved to /home/tarik/'file_name'")
