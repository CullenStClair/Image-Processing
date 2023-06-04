from argparse import ArgumentParser

import numpy as np
import PIL.Image as Image


def main():

    args = parse_args()


def parse_args():
    """Parse command-line arguments, handling multiple sub-commands with options:

    grayscale-----
    threshold-----
    sepia
    blur
    sharpen
    edge
    merge-----
    mirrorV-----
    mirrorH-----
    rotateCW-----
    rotateCCW-----
    crop-----
    resize
    matrix
    chain
    """

    parser = ArgumentParser(description="Simple image processing")

    parser.add_argument('input', metavar="<input-file>", help='Input image file path')
    parser.add_argument('output', metavar="<output-file>", help='Output image file name')

    # Setting dest='operation' means that the Namespace returned from
    # parse_args() will contain an attribute called 'operation' which
    # indicates which sub-command was specified
    subparsers = parser.add_subparsers(help='Operation', dest='operation', required=True)

    parser_op_grayscale = subparsers.add_parser('grayscale', help='Grayscale the image')
    parser_op_threshold = subparsers.add_parser('threshold', help='Threshold filter the image')
    parser_op_sepia = subparsers.add_parser('sepia', help='Sepia filter the image')
    parser_op_blur = subparsers.add_parser('blur', help='Box blur the image')
    parser_op_sharpen = subparsers.add_parser('sharpen', help='Sharpen the image')
    parser_op_edge = subparsers.add_parser('edge', help='Apply edge detection to the image')
    parser_op_merge = subparsers.add_parser('merge', help='Merge two images')
    parser_op_mirrorV = subparsers.add_parser('mirrorV', help='Mirror the image across the vertical axis')
    parser_op_mirrorH = subparsers.add_parser('mirrorH', help='Mirror the image across the horizontal axis')
    parser_op_rotateCW = subparsers.add_parser('rotateCW', help='Rotate the image clockwise')
    parser_op_rotateCCW = subparsers.add_parser('rotateCCW', help='Rotate the image counter-clockwise')
    parser_op_crop = subparsers.add_parser('crop', help='Crop the image')
    parser_op_resize = subparsers.add_parser('resize', help='Resize the image')
    parser_op_matrix = subparsers.add_parser('matrix', help='Apply a matrix to the image')
    parser_op_chain = subparsers.add_parser('chain', help='Chain multiple operations together')

    return parser.parse_args()


if __name__ == "__main__":
    main()
