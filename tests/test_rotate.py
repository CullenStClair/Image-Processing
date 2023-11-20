#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import unittest

import numpy as np
from PIL import Image

from operations import rotate


class TestCrop(unittest.TestCase):
    """Test the rotate operation"""

    @classmethod
    def setUpClass(cls):
        # Load the test image
        cls.img = np.array(Image.open('tests/tiny_test.png'))

    def test_rotate_cw(self):
        """Test a clockwise rotation"""

        actual = rotate(self.img)
        expected = np.rot90(self.img, 1, (1, 0))

        self.assertTrue(np.array_equal(actual, expected))

    def test_rotate_ccw(self):
        """Test a counterclockwise rotation"""

        actual = rotate(self.img, ccw=True)
        expected = np.rot90(self.img, 1, (0, 1))

        self.assertTrue(np.array_equal(actual, expected))

    def test_rotate_180(self):
        """Test a 180 degree rotation"""

        actual = rotate(self.img, 2)
        expected = np.rot90(self.img, 2)

        self.assertTrue(np.array_equal(actual, expected))


if __name__ == '__main__':
    unittest.main()
