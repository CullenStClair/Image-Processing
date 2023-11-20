#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

import numpy as np

from main import perform_operation


def chain(img: np.ndarray, operations: list[str]) -> np.ndarray:
    """Apply multiple operations to the image in sequence

    Args:
        img (np.ndarray): The image to apply the operations to
        operations (list[str]): The operations to apply to the image

    Returns:
        np.ndarray: The image after the operations have been applied
    """

    for operation in operations:
        if operation in ['composite', 'crop', 'chain']:
            raise ValueError(f"Operation {operation} is not supported in chain mode")
        else:
            img = perform_operation(img, operation)

    return img
