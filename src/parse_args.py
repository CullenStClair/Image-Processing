#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE.txt for more information

from argparse import ArgumentParser, ArgumentTypeError, Namespace


def parse_args() -> Namespace:
    """Parse command-line arguments, handling multiple sub-commands with options.

    boxblur       [-r, --radius <blur-radius>] [-i, --iterations <iterations>]
    chain         <operation> [<operation> ...]
    composite     <input-file-2> [-a, --alpha <alpha-value>] [-o, --offset <x-offset> <y-offset>]
    concat        [input-file-2] {--above | --below | --left | --right} {--scale | --crop | --fill}
    crop          <x1> <y1> <x2> <y2>
    edge          [-t, --thin]
    grayscale     
    invert
    kernel        <kernel-file> [-i, --iterations <iterations>]
    mirrorV
    mirrorH
    resize        <width> <height>
    rotateCW      [-t, --turns <turns>]
    rotateCCW     [-t, --turns <turns>]
    sepia         
    sharpen       [-s, --strength <sharpness-strength>]
    threshold     [-t, --threshold <threshold-value>] [-i, --invert]
    """

    parser = ArgumentParser(description="Simple image processing")

    # Common required arguments
    parser.add_argument("in_file", metavar="<image-path>", help="Input image file path")
    parser.add_argument("out_file", metavar="<output-file>",
                        help="Output image name with file extension (saved in same directory as input file)")

    # Setting dest="operation" means that the Namespace returned from
    # parse_args() will contain an attribute called "operation" which
    # indicates which sub-command was specified
    subparsers = parser.add_subparsers(dest="operation", required=True, help="Operation")

    # Sub-commands
    # Boxblur
    parser_op_boxblur = subparsers.add_parser("boxblur", help="Blur the image with a box blur")
    parser_op_boxblur.add_argument("-r", "--radius", metavar="<blur-radius>", type=_positive_int,
                                   default=1, help="Radius of pixel sampling (default: 1)")
    parser_op_boxblur.add_argument("-i", "--iterations", metavar="<blur-iterations>",
                                   type=_positive_int, default=1, help="Number of blur passes (default: 1)")

    # Chain (only operations that do not require additional arguments can be chained)
    # Valid operations: grayscale, threshold, sepia, blur, sharpen, edge, invert, mirrorV, mirrorH, rotateCW, rotateCCW
    parser_op_chain = subparsers.add_parser("chain", help="Apply multiple operations (without arguments) to the image")
    parser_op_chain.add_argument("operations", metavar="<operation>", nargs="+", help="Operations to apply in sequence",
                                 choices=["grayscale", "threshold", "sepia", "blur", "sharpen", "edge",
                                          "invert", "mirrorV", "mirrorH", "rotateCW", "rotateCCW"])

    # Composite
    parser_op_merge = subparsers.add_parser("composite", help="Composite an image over another")
    parser_op_merge.add_argument("in_file2", metavar="<top-image-path>",
                                 help="File path of image to be placed over first image")
    parser_op_merge.add_argument("-a", "--alpha", metavar="<alpha-value>", type=_valid_alpha,
                                 default=0.5, help="Transparency of top image [0-1] (default: 0.5)")
    parser_op_merge.add_argument("-o", "--offset", metavar="<x-offset> <y-offset>", nargs=2, type=int,
                                 default=[0, 0], help="Offset of top image from top-left corner of bottom image (default: 0 0)")

    # Concat
    parser_op_concat = subparsers.add_parser("concat", help="Concatenate two images or tile the same image")
    # The second image is optional, in which case the first image is tiled
    parser_op_concat.add_argument("in_file2", metavar="<second-image-path>", default=None,
                                  nargs="?", help="File path of image to be placed next to first image (optional)")
    placement_group = parser_op_concat.add_mutually_exclusive_group(required=True)
    # Where to place the second image relative to the first image
    placement_group.add_argument("--above", action="store_const", dest="placement",
                                 const="above", help="Place image 2 above image 1")
    placement_group.add_argument("--below", action="store_const", dest="placement",
                                 const="below", help="Place image 2 below image 1")
    placement_group.add_argument("--left", action="store_const", dest="placement",
                                 const="left", help="Place image 2 to the left of image 1")
    placement_group.add_argument("--right", action="store_const", dest="placement",
                                 const="right", help="Place image 2 to the right of image 1")
    mode_group = parser_op_concat.add_mutually_exclusive_group(required=True)
    # How to handle the second image if it does not fit exactly
    mode_group.add_argument("--scale", action="store_const", dest="mode", const="scale",
                            help="Scale the second image to match the bordering dimension of the first image")
    mode_group.add_argument("--crop", action="store_const", dest="mode", const="crop",
                            help="Crop the second image to match the bordering dimension of the first image")
    mode_group.add_argument("--fill", action="store_const", dest="mode", const="fill",
                            help="Fill unused space with the average colour of the second image")

    # Crop
    parser_op_crop = subparsers.add_parser("crop", help="Crop the image to within the given coordinates")
    parser_op_crop.add_argument("x1", metavar="<x1>", type=_non_negative_int, help="X coordinate of top-left corner")
    parser_op_crop.add_argument("y1", metavar="<y1>", type=_non_negative_int, help="Y coordinate of top-left corner")
    parser_op_crop.add_argument("x2", metavar="<x2>", type=_non_negative_int,
                                help="X coordinate of bottom-right corner")
    parser_op_crop.add_argument("y2", metavar="<y2>", type=_non_negative_int,
                                help="Y coordinate of bottom-right corner")

    # Edge
    parser_op_edge = subparsers.add_parser("edge", help="Apply edge detection to the image")
    parser_op_edge.add_argument("-t", "--thin", action="store_true", default=False,
                                help="Apply edge thinning post-processing")

    # Grayscale
    parser_op_grayscale = subparsers.add_parser("grayscale", help="Grayscale the image")

    # Invert
    parser_op_invert = subparsers.add_parser("invert", help="Invert the image colours")

    # Kernel
    parser_op_kernel = subparsers.add_parser("kernel", help="Perform a convolution on the image with the given kernel")
    parser_op_kernel.add_argument("kernel_file", metavar="<kernel-file>",
                                  help="File path of kernel/matrix to use in convolution (comma-separated values in .txt/.csv)")
    parser_op_kernel.add_argument("-i", "--iterations", metavar="<iterations>", type=_positive_int, default=1,
                                  help="Number of convolution passes (default: 1)")

    # Mirror vertical and horizontal
    parser_op_mirrorV = subparsers.add_parser("mirrorV", help="Mirror the image about the vertical axis")
    parser_op_mirrorH = subparsers.add_parser("mirrorH", help="Mirror the image about the horizontal axis")

    # Resize
    parser_op_resize = subparsers.add_parser("resize", help="Resize the image to the given dimensions")
    parser_op_resize.add_argument("width", metavar="<width>", type=_positive_int, help="New image width")
    parser_op_resize.add_argument("height", metavar="<height>", type=_positive_int, help="New image height")

    # Rotate clockwise and counter-clockwise
    parser_op_rotateCW = subparsers.add_parser("rotateCW", help="Rotate the image 90 degrees clockwise")
    parser_op_rotateCW.add_argument("-t", "--turns", metavar="<turns>", type=_positive_int,
                                    default=1, help="Number of clockwise turns (default: 1)")
    parser_op_rotateCCW = subparsers.add_parser("rotateCCW", help="Rotate the image 90 degrees counter-clockwise")
    parser_op_rotateCCW.add_argument("-t", "--turns", metavar="<turns>", type=_positive_int,
                                     default=1, help="Number of counter-clockwise turns (default: 1)")

    # Sepia
    parser_op_sepia = subparsers.add_parser("sepia", help="Sepia tone the image")

    # Sharpen
    parser_op_sharpen = subparsers.add_parser("sharpen", help="Sharpen the image")
    parser_op_sharpen.add_argument("-s", "--strength", metavar="<multiplier>",
                                   type=_positive_float, default=5, help="Sharpening strength multiplier (default: 5)")

    # Threshold
    parser_op_threshold = subparsers.add_parser("threshold", help="Threshold filter the image")
    parser_op_threshold.add_argument("-t", "--threshold", metavar="<threshold-value>", type=int,
                                     choices=range(0, 256), default=128, help="Threshold value [0-255] (default: 128)")
    parser_op_threshold.add_argument("-i", "--invert", action="store_true",
                                     default=False, help="Invert the threshold operation (above threshold -> black)")

    return parser.parse_args()


def _non_negative_int(value):
    """Check that the value is a non-negative integer"""
    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid non-negative int value")
    if ivalue < 0:
        raise ArgumentTypeError(f"'{value}' is an invalid non-negative int value")
    return ivalue


def _positive_int(value):
    """Check that the value is a positive integer"""
    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid positive int value")
    if ivalue <= 0:
        raise ArgumentTypeError(f"'{value}' is an invalid positive int value")
    return ivalue


def _positive_float(value):
    """Check that the value is a positive float"""
    try:
        fvalue = float(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid positive float value")
    if fvalue <= 0:
        raise ArgumentTypeError(f"'{value}' is an invalid positive float value")
    return fvalue


def _valid_alpha(value):
    """Check that the value is a float in the range [0, 1]"""
    try:
        fvalue = float(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid alpha value (must be in range [0, 1])")
    if fvalue < 0 or fvalue > 1:
        raise ArgumentTypeError(f"'{value}' is an invalid alpha value (must be in range [0, 1])")
    return fvalue
