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
from utils import get_file_size, get_kernel_from_terminal


def main():

    # Parse command line arguments
    args = parse_args()

    # Handle input file path
    in_file = Path(args.in_file)
    if not in_file.is_file():  # Check if input file exists
        print(f'File not found: {in_file}')
        exit(1)

    # Read the input image contents into a numpy array
    try:
        with Image.open(in_file) as img_file:  # reconsider use of context manager within try block
            img = np.array(img_file, dtype=np.uint8)
            print(f'Loaded image: {in_file.name} ({img.shape[1]}x{img.shape[0]}), {get_file_size(in_file)}')

    except UnidentifiedImageError:
        print(f'File is not a valid image: {in_file}')
        exit(1)

    # Perform the requested operation(s)
    try:
        img = perform_operation(img, args.operation, args)

    except ValueError as e:
        print('[ERROR]', e)
        print('Use the --help flag for usage information about the requested operation.')
        print('Exiting...')
        exit(1)

    # Get output file path
    out_file = in_file.parent.joinpath(args.out_file)  # Output to same directory as input file
    i = 1  # If output file already exists, append number to filename
    stem = out_file.stem
    while out_file.exists():
        out_file = in_file.parent.joinpath(f'{stem}-{i}{out_file.suffix}')
        i += 1

    # Save the output image
    try:
        with Image.fromarray(img) as img_file:
            img_file.save(out_file)
            print(f'Saved image: {out_file.name} ({img.shape[1]}x{img.shape[0]}), {get_file_size(out_file)}')

    except ValueError:
        print(f'Unrecognized output format: {out_file.suffix}')
        exit(1)

    except OSError:
        print(f'Unable to save file: {out_file}')

        if '/' in args.out_file or '\\' in args.out_file:  # Warn about invalid file path
            print("Output file path may be invalid. Relative paths begin from the input file's directory.")

        if img.shape[2] == 4 and out_file.suffix.lower() not in ['.png', '.tiff']:  # Warn about transparency
            print('Image has transparency. Try saving as another format (e.g. PNG)')

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

    print(f'Performing operation: {op_name}')

    # check for None args to use default arguments
    # this allows the perform_operation function to be re-used for chaining
    match op_name:
        case 'boxblur':
            if args is None:
                img = op.box_blur(img)
            else:
                img = op.box_blur(img, args.radius, args.passes)

        case 'chain':
            if args is None:
                raise ValueError('Chain operation requires arguments')
            else:
                img = op.chain(img, args.operations)

        case 'composite':
            if args is None:
                raise ValueError('Composite operation requires arguments')
            else:
                pass

        case 'crop':
            if args is None:
                raise ValueError('Crop operation requires arguments')
            else:
                img = op.crop(img, args.x1, args.y1, args.x2, args.y2)

        case 'edge':
            if args is None:
                img = op.edge(img)
            else:
                img = op.edge(img, args.threshold)

        case 'grayscale':
            img = op.grayscale(img)

        case 'invert':
            img = op.invert(img)

        case 'convolve':
            if args is None:
                kernel = get_kernel_from_terminal(3)
                img = op.convolve(img, kernel)
            else:
                kernel = get_kernel_from_terminal(args.kernel_size)
                img = op.convolve(img, kernel, args.iterations)

        case 'mirrorH':
            img = op.mirror(img)

        case 'mirrorV':
            img = op.mirror(img, vertical=True)

        case 'rotateCW':
            if args is None:
                img = op.rotate(img)
            else:
                img = op.rotate(img, args.turns)

        case 'rotateCCW':
            if args is None:
                img = op.rotate(img, ccw=True)
            else:
                img = op.rotate(img, args.turns, ccw=True)

        case 'sepia':
            pass

        case 'sharpen':
            if args is None:
                img = op.sharpen(img)
            else:
                img = op.sharpen(img, args.amount)

        case 'threshold':
            if args is None:
                img = op.threshold(img)
            else:
                img = op.threshold(img, args.threshold, args.binary, args.invert)

        case _:
            raise ValueError(f'Unrecognized operation: {op_name}')

    return img


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting...')
        exit(0)
