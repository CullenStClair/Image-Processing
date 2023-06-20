#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np
from scipy.signal import convolve2d


def convolve(img: np.ndarray, kernel: np.ndarray, passes: int = 1) -> np.ndarray:
    """Convolves an image with a kernel.

    Args:
        img (np.ndarray): The image to convolve
        kernel (np.ndarray): The kernel to convolve with
        passes (int, optional): The number of times to convolve the image. Defaults to 1

    Returns:
        np.ndarray: The convolved image
    """

    # Ensure the kernel is square and is odd-sized
    if kernel.shape[0] != kernel.shape[1] or kernel.shape[0] % 2 == 0:
        raise ValueError("Kernel must be an odd-sized square")

    # Flip the kernel in both axes (convolution is equivalent to correlation with a flipped kernel)
    kernel = np.flip(kernel)

    # Promote array types
    img = img.astype(np.float64)
    kernel = kernel.astype(np.float64)

    # Extract colour channels from the image
    red = img[..., 0]
    green = img[..., 1]
    blue = img[..., 2]
    if img.shape[2] == 4:
        alpha = img[..., 3]
    else:
        alpha = None

    # Perform the convolution
    for _ in range(passes):
        red = convolve2d(red, kernel, mode="same", boundary="symm")
        green = convolve2d(green, kernel, mode="same", boundary="symm")
        blue = convolve2d(blue, kernel, mode="same", boundary="symm")

    # Recombine colour channels
    img = np.dstack((red, green, blue))

    # Add the alpha channel back in if necessary
    if alpha is not None:
        img = np.dstack((img, alpha))

    # Convert back to uint8 from float64
    return img.astype(np.uint8)
