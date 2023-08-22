#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np

from .convolve import convolve


def sharpen(img: np.ndarray, amount: float = 3) -> np.ndarray:
    """Sharpen an image using unsharp masking.

    Args:
        img (np.ndarray): The image to sharpen
        amount (float): The strength of the sharpening effect

    Returns:
        np.ndarray: The sharpened image
    """

    # Create the "original" kernel which does not change the image
    original = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    # Create the "blurred" kernel using 5 pixels for sampling
    blurred = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]) / 5

    # Create the unsharp masking kernel using a typical formula
    kernel = original + (original - blurred) * amount

    # Apply the kernel to the image
    return convolve(img, kernel)
