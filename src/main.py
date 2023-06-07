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
        with Image.open(in_file) as img:
            img_arr = np.array(img, dtype="uint8")
    except FileNotFoundError:
        print(f"File not found: {in_file}")
        exit(1)
    except UnidentifiedImageError:
        print(f"File is not a valid image: {in_file}")
        exit(1)

    # Check if the image has an alpha channel
    has_alpha = True if img_arr.shape[2] == 4 else False

    # Perform the requested operation
    if args.operation == "boxblur":
        pass
    elif args.operation == "chain":
        pass
    elif args.operation == "composite":
        pass
    elif args.operation == "concat":
        pass
    elif args.operation == "crop":
        pass
    elif args.operation == "edge":
        pass
    elif args.operation == "grayscale":
        img_arr = op.grayscale(img_arr, has_alpha)
    elif args.operation == "invert":
        pass
    elif args.operation == "kernel":
        pass
    elif args.operation == "mirrorV":
        pass
    elif args.operation == "mirrorH":
        pass
    elif args.operation == "resize":
        pass
    elif args.operation == "rotateCW":
        pass
    elif args.operation == "rotateCCW":
        pass
    elif args.operation == "sepia":
        pass
    elif args.operation == "sharpen":
        pass
    elif args.operation == "threshold":
        pass

    # Get output file path
    out_file = in_file.parent.joinpath(args.out_file)  # Output to same directory as input file
    i = 1  # If output file already exists, append number to filename
    stem = out_file.stem
    while out_file.exists():
        out_file = in_file.parent.joinpath(f"{stem}-{i}{out_file.suffix}")
        i += 1

    # Save the output image
    try:
        with Image.fromarray(img_arr) as img:
            img.save(out_file)
    except ValueError:
        print(f"Unrecognized output format: {out_file.suffix}")
        exit(1)
    except OSError:
        print(f"Unable to save file: {out_file}")
        if has_alpha:
            print("Image has transparency. Try saving as another format")
        exit(1)


if __name__ == "__main__":
    main()
