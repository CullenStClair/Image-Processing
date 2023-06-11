from argparse import Namespace
from pathlib import Path

import numpy as np
from PIL import Image, UnidentifiedImageError

import operations as op
from parse_args import parse_args


def main():

    # Parse command line arguments
    args = parse_args()

    # Handle input file path
    in_file = Path(args.in_file)
    if not in_file.is_file():  # Check if input file exists
        print(f"File not found: {in_file}")
        exit(1)

    # Read the input image contents into a numpy array
    try:
        with Image.open(in_file) as img_file:
            img = np.array(img_file, dtype="uint8")
            print(f"Loaded image: {in_file.name} ({img.shape[1]}x{img.shape[0]}), {in_file.stat().st_size} bytes")
    except UnidentifiedImageError:
        print(f"File is not a valid image: {in_file}")
        exit(1)

    # Perform the requested operation(s)
    try:
        img = perform_operation(img, args.operation, args)
    except ValueError as e:
        print("[ERROR]", e)
        print("Use the --help flag for usage information")
        print("Exiting...")
        exit(1)

    # Get output file path
    out_file = in_file.parent.joinpath(args.out_file)  # Output to same directory as input file
    i = 1  # If output file already exists, append number to filename
    stem = out_file.stem
    while out_file.exists():
        out_file = in_file.parent.joinpath(f"{stem}-{i}{out_file.suffix}")
        i += 1

    # Save the output image
    try:
        with Image.fromarray(img) as img_file:
            img_file.save(out_file)
        print(f"Saved image: {out_file.name} ({img.shape[1]}x{img.shape[0]}), {out_file.stat().st_size} bytes")
    except ValueError:
        print(f"Unrecognized output format: {out_file.suffix}")
        exit(1)
    except OSError:
        print(f"Unable to save file: {out_file}")
        if img.shape[2] == 4:  # Check if image has alpha channel
            print("Image has transparency. Try saving as another format (e.g. PNG)")
        exit(1)


def perform_operation(img: np.ndarray, op_name: str, args: Namespace) -> np.ndarray:
    """Performs the requested operation on the image array.

    Args:
        op_name (str): The name of the operation to perform
        img (np.ndarray): The image array to perform the operation on
        args: The arguments to pass to the operation

    Returns:
        np.ndarray: The image array after the operation has been performed
    """
    print(f"Performing operation: {op_name}")

    match op_name:
        case "boxblur":
            pass

        case "chain":
            pass

        case "composite":
            pass

        case "concat":
            pass

        case "crop":
            img = op.crop(img, args.x1, args.y1, args.x2, args.y2)

        case "edge":
            pass

        case "grayscale":
            img = op.grayscale(img)

        case "invert":
            pass

        case "kernel":
            pass

        case "mirrorV":
            pass

        case "mirrorH":
            pass

        case "resize":
            pass

        case "rotateCW":
            pass

        case "rotateCCW":
            pass

        case "sepia":
            pass

        case "sharpen":
            pass

        case "threshold":
            pass

        case _:
            print(f"Unrecognized operation: {op_name}")
            exit(1)

    return img


if __name__ == "__main__":
    main()
