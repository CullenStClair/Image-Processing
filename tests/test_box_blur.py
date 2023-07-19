#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import unittest

import numpy as np
from PIL import Image

from operations import box_blur


class TestBoxBlur(unittest.TestCase):
    """Test the box blur operation"""

    @classmethod
    def setUpClass(cls):
        # Load the test image
        cls.img = np.array(Image.open("tests/tiny_test.png"))

    def test_normal_case(self):
        """Test a normal case (radius = 1, passes = 1)"""

        actual = box_blur(self.img)

        with self.subTest("Red channel"):
            actual_r = actual[..., 0]
            expected_r = np.array(
                [[0, 85, 170],
                 [28, 85, 141],
                 [56, 85, 113]])
            self.assertTrue(np.array_equal(actual_r, expected_r))

        with self.subTest("Green channel"):
            actual_g = actual[..., 1]
            expected_g = np.array(
                [[0, 28, 56],
                 [85, 85, 85],
                 [170, 141, 113]])
            self.assertTrue(np.array_equal(actual_g, expected_g))

        with self.subTest("Blue channel"):
            actual_b = actual[..., 2]
            expected_b = np.array(
                [[255, 198, 141],
                 [198, 170, 141],
                 [141, 141, 141]])
            self.assertTrue(np.array_equal(actual_b, expected_b))

        with self.subTest("Alpha channel"):
            actual_a = actual[..., 3]
            expected_a = np.full((3, 3), 255, dtype=np.uint8)
            self.assertTrue(np.array_equal(actual_a, expected_a))


if __name__ == "__main__":
    unittest.main()
