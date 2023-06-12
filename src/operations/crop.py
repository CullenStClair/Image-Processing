#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE.txt for more information

import numpy as np


def crop(img: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    """Crops the image to within the specified coordinates.

    Args:
        img (np.ndarray):  The image to crop
        x1 (int): The x-coordinate of the top left corner
        y1 (int): The y-coordinate of the top left corner
        x2 (int): The x-coordinate of the bottom right corner
        y2 (int): The y-coordinate of the bottom right corner

    Raises:
        ValueError: If the coordinates are invalid

    Returns:
        np.ndarray: The cropped image
    """

    # Image dimensions (upper bounds for coordinates)
    height = img.shape[0]
    width = img.shape[1]

    # Validate coordinates
    if x1 < 0 or y1 < 0 or x1 > width or y1 > height:
        raise ValueError(f"Invalid top left coordinates: ({x1}, {y1})")

    elif x2 < 0 or y2 < 0 or x2 > width or y2 > height:
        raise ValueError(f"Invalid bottom right coordinates: ({x2}, {y2})")

    elif x1 > x2 or y1 > y2:
        raise ValueError(f"Invalid coordinates: ({x1}, {y1}) is not above and to the left of ({x2}, {y2})")

    # Crop the image (first dimension is height-wise, second is width-wise)
    return img[y1:y2 + 1, x1:x2 + 1]
