import numpy as np
from PIL import Image

def generate_colors():
    colors = []
    for r in range(8, 257, 8):
        for g in range(8, 257, 8):
            for b in range(8, 257, 8):
                colors.append((r, g, b))
    np.random.shuffle(colors)
    return colors

def create_image(colors, width, height, pixel_size):
    image = Image.new('RGB', (width * pixel_size, height * pixel_size))
    pixels = image.load()

    for i, color in enumerate(colors):
        x = (i % width) * pixel_size
        y = (i // width) * pixel_size
        for j in range(pixel_size):
            for k in range(pixel_size):
                pixels[x + j, y + k] = color

    return image