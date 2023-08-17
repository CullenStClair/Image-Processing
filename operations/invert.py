#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np


def invert(img: np.ndarray) -> np.ndarray:
    """Inverts the image colours.

    Args:
        img (np.ndarray): The image to invert

    Returns:
        np.ndarray: The inverted image
    """

    # Extract the alpha channel if necessary
    if img.shape[2] == 4:
        alpha = img[..., 3]

    # Invert the image
    inverted = 255 - img[..., :3]

    # Add the alpha channel back in if necessary
    if img.shape[2] == 4:
        inverted = np.dstack((inverted, alpha))

    return inverted
