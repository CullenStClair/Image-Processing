import numpy as np


def grayscale(img: np.ndarray, has_alpha: bool) -> np.ndarray:
    """Converts the image to grayscale. 
        img: The image array to convert 
        has_alpha: Whether the image has an alpha channel
        return: The grayscaled image array (uint8)
    """
    # Average of all colour channels weighted equally for simple grayscale
    gray = np.mean(img[..., :3], axis=2)

    # Altenative for gamma-corrected grayscale (weighted channels)
    # gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

    # Add the alpha channel back in if necessary
    if has_alpha:
        alpha = img[:, :, 3]
        gray = np.dstack((gray, alpha))

    # Convert back to uint8 from float64
    return gray.astype(np.uint8)
