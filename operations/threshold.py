#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np


def threshold(img: np.ndarray, value: int = 128, invert: bool = False) -> np.ndarray:
    """Applies a threshold to an image.

    Args:
        img (np.ndarray): The image to apply the threshold to
        value (int, optional): The threshold value. Defaults to 128
        invert (bool, optional): Whether to invert the threshold. Defaults to False

    Returns:
        np.ndarray: The thresholded image
    """

    # Ensure the threshold value is in the range [0, 255]
    if value < 0 or value > 255:
        raise ValueError("Threshold value must be in the range [0, 255]")

    # Extract colour channels from the image
    red = img[..., 0]
    green = img[..., 1]
    blue = img[..., 2]

    # Extract alpha channel if necessary
    if img.shape[2] == 4:
        alpha = img[..., 3]
    else:
        alpha = None

    # Apply the threshold
    red = np.where(red < value, 0, 255)
    green = np.where(green < value, 0, 255)
    blue = np.where(blue < value, 0, 255)

    # Recombine colour channels
    img = np.dstack((red, green, blue))

    # Add the alpha channel back in if necessary
    if alpha is not None:
        img = np.dstack((img, alpha))

    # Invert the threshold if specified
    if invert:
        img = 255 - img

    return img
