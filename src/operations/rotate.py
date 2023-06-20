#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np


def rotate(img: np.ndarray, turns: int = 1, ccw: bool = False) -> np.ndarray:
    """Rotates the image in 90 degree increments.

    Args:
        img (np.ndarray): The image to rotate
        CCW (bool, optional): Whether to rotate the image counterclockwise. Defaults to False
        turns (int, optional): The number of 90 degree turns to rotate the image. Defaults to 1

    Returns:
        np.ndarray: The rotated image
    """

    # If rotating CW, negate turns (np.rot90 rotates CCW by default)
    if not ccw:
        turns = -turns

    return np.rot90(img, turns)
