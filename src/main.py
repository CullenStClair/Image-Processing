from pathlib import Path

import numpy as np
from PIL import Image, UnidentifiedImageError

from parse_args import parse_args


def main():

    args = parse_args()

    # Handle guaranteed file path arguments
    in_file = Path(args.in_file)
    if not in_file.is_file():  # check if input file exists
        print(f"File not found: {in_file}")
        exit(1)
    out_file = in_file.parent.joinpath(args.out_file)  # output to same directory as input file
    i = 1  # if output file already exists, append number to filename
    stem = out_file.stem
    while out_file.exists():
        out_file = in_file.parent.joinpath(f"{stem}-{i}{out_file.suffix}")
        i += 1

    # read the input image contents into a numpy array
    try:
        with Image.open(in_file) as img:
            img_arr = np.array(img)
    except FileNotFoundError:
        print(f"File not found: {in_file}")
        exit(1)
    except UnidentifiedImageError:
        print(f"File is not a valid image: {in_file}")
        exit(1)

    # check if the image has an alpha channel
    has_alpha = True if img_arr.shape[2] == 4 else False

    # save the output image
    try:
        with Image.fromarray(img_arr) as img:
            img.save(out_file)
    except ValueError:
        print(f"Unrecognized output format: {out_file.suffix}")
        exit(1)
    except OSError:
        print(f"Unable to save file: {out_file}")
        if has_alpha:
            print("Input image has transparency: Try saving as .png or .webp")
        exit(1)


if __name__ == "__main__":
    main()
