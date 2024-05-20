import unittest
from app.utils import generate_colors, create_image

class TestUtils(unittest.TestCase):
    def test_generate_colors(self):
        colors = generate_colors()
        self.assertEqual(len(colors), 32768)
        self.assertEqual(len(set(colors)), 32768)

    def test_create_image(self):
        colors = generate_colors()
        width = 128
        height = 256
        pixel_size = 4
        image = create_image(colors, width, height, pixel_size)
        self.assertEqual(image.size, (width * pixel_size, height * pixel_size))

    def test_color_components(self):
        colors = generate_colors()
        for color in colors:
            self.assertGreaterEqual(color[0], 8)
            self.assertLessEqual(color[0], 256)
            self.assertGreaterEqual(color[1], 8)
            self.assertLessEqual(color[1], 256)
            self.assertGreaterEqual(color[2], 8)
            self.assertLessEqual(color[2], 256)
            self.assertEqual(color[0] % 8, 0)
            self.assertEqual(color[1] % 8, 0)
            self.assertEqual(color[2] % 8, 0)

if __name__ == '__main__':
    unittest.main()