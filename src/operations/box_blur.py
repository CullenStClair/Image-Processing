#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np

from .convolve import convolve


def box_blur(img: np.ndarray, radius: int = 1, passes: int = 1) -> np.ndarray:
    """Blurs an image using a box blur.

    Args:
        img (np.ndarray): The image to blur
        radius (int, optional): The radius of pixels to sample for blurring. Defaults to 1, max 5
        passes (int, optional): The number of times to apply the blur. Defaults to 1

    Returns:
        np.ndarray: The blurred image
    """

    if radius > 5:
        raise ValueError("Radius should be at most 5")

    # Create the kernel with the specified radius (all pixels are equally weighted)
    kernel_size = radius * 2 + 1
    kernel = np.full((kernel_size, kernel_size), 1 / kernel_size ** 2)

    return convolve(img, kernel, passes)
