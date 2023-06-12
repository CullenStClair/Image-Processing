#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE.txt for more information

import numpy as np


def grayscale(img: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale using an unweighted average of colour channels.

    Args:
        img (np.ndarray): The image to convert to grayscale
        has_alpha (bool): Whether the image has an alpha channel

    Returns:
        np.ndarray: The grayscale image
    """

    # Average of all colour channels weighted equally for simple grayscale
    gray = np.mean(img[..., :3], axis=2)

    # Altenative for gamma-corrected grayscale (weighted channels)
    # gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

    # Add the alpha channel back in if necessary
    if img.shape[2] == 4:
        alpha = img[..., 3]
        gray = np.dstack((gray, gray, gray, alpha))

    # Convert back to uint8 from float64
    return gray.astype(np.uint8)
