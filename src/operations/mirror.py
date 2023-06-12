#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np


def mirror(img: np.ndarray, vertical: bool = False):
    """Mirrors the image across the vertical or horizontal axis

    Args:
        img (np.ndarray): The image to mirror
        horizontal (bool, optional): Whether to mirror the image across the horizontal axis. Defaults to False

    Returns:
        np.ndarray: The mirrored image
    """

    if vertical:
        return np.flipud(img)
    else:
        return np.fliplr(img)
