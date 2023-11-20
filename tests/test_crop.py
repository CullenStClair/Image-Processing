#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import unittest

import numpy as np
from PIL import Image

from operations import crop


class TestCrop(unittest.TestCase):
    """Test the crop operation"""

    @classmethod
    def setUpClass(cls):
        # Load the test image
        cls.img = np.array(Image.open('tests/tiny_test.png'))

    def test_no_crop(self):
        """Test a crop that does nothing"""

        actual = crop(self.img, 0, 0, 3, 3)
        expected = self.img

        self.assertTrue(np.array_equal(actual, expected))

    def test_centre_crop(self):
        """Test a crop that removes some pixels from all sides"""

        actual = crop(self.img, 1, 1, 2, 2)
        expected = np.array([[[0, 0, 255, 255]]])

        self.assertTrue(np.array_equal(actual, expected))

    def test_crop_to_right_edge(self):
        """Test a crop that leaves the rightmost column"""

        actual = crop(self.img, 2, 0, 3, 3)
        expected = np.array(
            [[[255, 0, 0, 255]],
             [[255, 255, 255, 255]],
             [[0, 0, 0, 255]]])

        self.assertTrue(np.array_equal(actual, expected))


if __name__ == '__main__':
    unittest.main()
