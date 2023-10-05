#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np


def composite(img_bottom: np.ndarray, img_top: np.ndarray, alpha: int, offset_x: int, offset_y: int) -> np.ndarray:
    """Composites an image over another (premultiplied alpha blending).

    Args:
        img_bottom (np.ndarray): The image to be placed under the other
        img_top (np.ndarray): The image to be placed over the other
        alpha (int): The transparency multiplier for the top image [0-1]
        offset_x (int): The x-coordinate of the top left corner of the top image (can be negative)
        offset_y (int): The y-coordinate of the top left corner of the top image (can be negative)

    Returns:
        np.ndarray: The composited image
    """
