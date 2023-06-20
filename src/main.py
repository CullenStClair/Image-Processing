#  A command line interface for common image editing tasks.
#  Copyright (C) 2023  Cullen St-Clair

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.

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
            print(f"Loaded image: {in_file.name} ({img.shape[1]}x{img.shape[0]}), {get_file_size(in_file)}")

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
            print(f"Saved image: {out_file.name} ({img.shape[1]}x{img.shape[0]}), {get_file_size(out_file)}")

    except ValueError:
        print(f"Unrecognized output format: {out_file.suffix}")
        exit(1)

    except OSError:
        print(f"Unable to save file: {out_file}")
        if img.shape[2] == 4:  # Check if image has alpha channel
            print("Image has transparency. Try saving as another format (e.g. PNG)")
        exit(1)


def perform_operation(img: np.ndarray, op_name: str, args: Namespace = None) -> np.ndarray:
    """Performs the requested operation on the image array.

    Args:
        op_name (str): The name of the operation to perform
        img (np.ndarray): The image array to perform the operation on
        args: The arguments to pass to the operation

    Returns:
        np.ndarray: The image array after the operation has been performed
    """

    # use default arguments if none are provided (only the case for chain operations)
    # this allows the perform_operation function to be re-used for the chain operation
    # argparse already rejects unsupported chain operations, so no need to check for them here

    print(f"Performing operation: {op_name}")

    match op_name:
        case "boxblur":
            if args is None:
                img = op.box_blur(img)
            else:
                img = op.box_blur(img, args.radius, args.passes)

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

        case "mirrorH":
            img = op.mirror(img)

        case "mirrorV":
            img = op.mirror(img, vertical=True)

        case "resize":
            pass

        case "rotateCW":
            if args is None:
                img = op.rotate(img)
            else:
                img = op.rotate(img, args.turns)

        case "rotateCCW":
            if args is None:
                img = op.rotate(img, ccw=True)
            else:
                img = op.rotate(img, args.turns, ccw=True)

        case "sepia":
            pass

        case "sharpen":
            pass

        case "threshold":
            pass

        case _:
            raise ValueError(f"Unrecognized operation: {op_name}")

    return img


def get_file_size(file: Path) -> str:
    """Returns the size of a file in relevant units.

    Args:
        file (Path): The file to get the size of

    Returns:
        str: The size of the file in relevant units
    """
    if not file.is_file():
        raise ValueError(f"File not found: {file}")

    size = file.stat().st_size
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{round(size / 1024, 1)} KB"
    elif size < 1024 ** 3:
        return f"{round(size / 1024 ** 2, 1)} MB"
    else:
        return f"{round(size / 1024 ** 3, 1)} GB"


if __name__ == "__main__":
    main()
