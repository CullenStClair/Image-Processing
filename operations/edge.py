#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np

from .convolve import convolve
from .grayscale import grayscale
from .threshold import threshold


def edge(img: np.ndarray, cutoff: int = 150) -> np.ndarray:
    """Applies edge detection to an image using a Sobel filter.

    Args:
        img (np.ndarray): The image to apply edge detection to
        cutoff (int, optional): The threshold to use for edge detection. Defaults to 150.

    Returns:
        np.ndarray: The edge-detected image
    """

    # Convert to grayscale
    img = grayscale(img)

    # Filter noise by blurring the image (approximate Gaussian blur)
    img = convolve(img, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16, passes=2)

    # Sobel kernels
    gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Convolve the image with the kernels
    img_x = convolve(img, gx)
    img_y = convolve(img, gy)

    # Combine the results by taking the magnitude of the gradient
    img = np.sqrt(img_x ** 2 + img_y ** 2)

    # Normalize the image
    img = img / np.max(img) * 255

    # Clip values to the range [0, 255]
    np.clip(img, 0, 255, out=img)

    # Threshold the image to reduce noise
    img = threshold(img, cutoff)

    # Convert back to uint8
    return img.astype(np.uint8)
