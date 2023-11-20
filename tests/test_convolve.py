#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import unittest

import numpy as np
from PIL import Image

from operations import convolve


class TestConvolve(unittest.TestCase):
    """Test the box blur operation"""

    @classmethod
    def setUpClass(cls):
        # Load the test image
        cls.img = np.array(Image.open('tests/tiny_test.png'))
        # Create a random test image
        cls.rand_img = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
        # Create identity kernel
        cls.identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float64)

    def test_identity_small_case(self):
        """Test with an identity kernel and small test image (passes = 1)"""

        actual = convolve(self.img, self.identity_kernel)
        self.assertTrue(np.array_equal(actual, self.img))

    def test_identity_large_case(self):
        """Test with an identity kernel and large test image (passes = 1)"""

        actual = convolve(self.rand_img, self.identity_kernel)
        self.assertTrue(np.array_equal(actual, self.rand_img))


if __name__ == '__main__':
    unittest.main()
