#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

from argparse import ArgumentParser, Namespace

from utils import non_negative_int, positive_float, positive_int, valid_alpha


def parse_args() -> Namespace:
    """Parse command-line arguments, handling multiple sub-commands with options.

    boxblur       [-r, --radius <blur-radius>] [-p, --passes <blur-passes>]
    chain         <operation> [<operation> ...]
    composite     <input-file-2> [-a, --alpha <alpha-value>] [-o, --offset <x-offset> <y-offset>]
    convolve        <kernel-size> [-i, --iterations <iterations>]
    crop          <x1> <y1> <x2> <y2>
    edge          [-t, --threshold <threshold-value>]
    grayscale     
    invert
    mirrorH
    mirrorV
    rotateCW      [-t, --turns <turns>]
    rotateCCW     [-t, --turns <turns>]
    sepia         
    sharpen       [-s, --strength <sharpness-strength>]
    threshold     [-t, --threshold <threshold-value>] [-b, --binary] [-i, --invert]
    """

    parser = ArgumentParser(description="A python program for image processing.")

    # Common required arguments
    parser.add_argument("in_file", metavar="<image-path>", help="Input image file path")
    parser.add_argument("out_file", metavar="<output-file>",
                        help="Output image name with file extension (saved in same directory as input file)")

    # Setting dest="operation" means that the Namespace returned from
    # parse_args() will contain an attribute called "operation" which
    # indicates which sub-command was specified
    subparsers = parser.add_subparsers(dest="operation", required=True, help="Operation")

    # Sub-command parsers
    # Boxblur
    parser_op_boxblur = subparsers.add_parser("boxblur", help="Blur the image with a box blur")
    parser_op_boxblur.add_argument("-r", "--radius", metavar="<blur-radius>", type=int, choices=range(1, 6),
                                   default=1, help="Radius of pixel sampling (default: 1, max: 5)")
    parser_op_boxblur.add_argument("-p", "--passes", metavar="<blur-passes>",
                                   type=positive_int, default=1, help="Number of times to apply blur (default: 1)")

    # Chain (crop, composite, and chain can't be used in chain mode)
    # Valid operations: grayscale, threshold, sepia, blur, sharpen, edge, invert, mirrorV, mirrorH, rotateCW, rotateCCW, convolve
    parser_op_chain = subparsers.add_parser("chain", help="Apply multiple operations (without arguments) to the image")
    parser_op_chain.add_argument("operations", metavar="<operation>", nargs="+", help="Operations to apply in sequence",
                                 choices=["grayscale", "threshold", "sepia", "blur", "sharpen", "edge",
                                          "invert", "mirrorV", "mirrorH", "rotateCW", "rotateCCW", "convolve"])

    # Composite
    parser_op_merge = subparsers.add_parser("composite", help="Composite an image over another")
    parser_op_merge.add_argument("in_file2", metavar="<top-image-path>",
                                 help="File path of image to be placed over first image")
    parser_op_merge.add_argument("-a", "--alpha", metavar="<alpha-value>", type=valid_alpha,
                                 default=0.5, help="Transparency of top image [0-1] (default: 0.5)")
    parser_op_merge.add_argument("-o", "--offset", metavar="<x-offset> <y-offset>", nargs=2, type=int,
                                 default=[0, 0], help="Offset of top image from top-left corner of bottom image (default: 0 0)")

    # Convolve
    parser_op_convolve = subparsers.add_parser(
        "convolve", help="Perform a convolution on the image with the given square kernel")
    parser_op_convolve.add_argument("kernel_size", metavar="<kernel-size>", type=positive_int, default=3,
                                    help="Side length of square kernel to use in convolution (default: 3)")
    parser_op_convolve.add_argument("-i", "--iterations", metavar="<iterations>", type=positive_int, default=1,
                                    help="Number of convolution passes (default: 1)")

    # Crop
    parser_op_crop = subparsers.add_parser("crop", help="Crop the image to within the given coordinates")
    parser_op_crop.add_argument("x1", metavar="<x1>", type=non_negative_int, help="X coordinate of top-left corner")
    parser_op_crop.add_argument("y1", metavar="<y1>", type=non_negative_int, help="Y coordinate of top-left corner")
    parser_op_crop.add_argument("x2", metavar="<x2>", type=non_negative_int,
                                help="X coordinate of bottom-right corner")
    parser_op_crop.add_argument("y2", metavar="<y2>", type=non_negative_int,
                                help="Y coordinate of bottom-right corner")

    # Edge
    parser_op_edge = subparsers.add_parser("edge", help="Apply edge detection to the image")
    parser_op_edge.add_argument("-t", "--threshold", metavar="<threshold-value>", type=int, choices=range(256),
                                default=150, help="Threshold value [0-255] (lower = more 'edges', default: 150)")

    # Grayscale
    parser_op_grayscale = subparsers.add_parser("grayscale", help="Grayscale the image")

    # Invert
    parser_op_invert = subparsers.add_parser("invert", help="Invert the image colours")

    # Mirror vertical and horizontal
    parser_op_mirrorH = subparsers.add_parser("mirrorH", help="Mirror the image horizontally")
    parser_op_mirrorV = subparsers.add_parser("mirrorV", help="Mirror the image vertically")

    # Rotate clockwise and counter-clockwise
    parser_op_rotateCW = subparsers.add_parser("rotateCW", help="Rotate the image 90 degrees clockwise")
    parser_op_rotateCW.add_argument("-t", "--turns", metavar="<turns>", type=positive_int,
                                    default=1, help="Number of clockwise turns (default: 1)")
    parser_op_rotateCCW = subparsers.add_parser("rotateCCW", help="Rotate the image 90 degrees counter-clockwise")
    parser_op_rotateCCW.add_argument("-t", "--turns", metavar="<turns>", type=positive_int,
                                     default=1, help="Number of counter-clockwise turns (default: 1)")

    # Sepia
    parser_op_sepia = subparsers.add_parser("sepia", help="Sepia tone the image")

    # Sharpen
    parser_op_sharpen = subparsers.add_parser("sharpen", help="Sharpen the image using unsharp masking")
    parser_op_sharpen.add_argument("-a", "--amount", metavar="<multiplier>",
                                   type=positive_float, default=3, help="Sharpening strength multiplier (default: 3)")

    # Threshold
    parser_op_threshold = subparsers.add_parser("threshold", help="Threshold filter the image")
    parser_op_threshold.add_argument("-t", "--threshold", metavar="<threshold-value>", type=int,
                                     choices=range(0, 256), default=128, help="Threshold cutoff value [0-255] (default: 128)")
    parser_op_threshold.add_argument("-b", "--binary", action="store_true", default=False,
                                     help="Perform binary segmentation (black and white, default: False)")
    parser_op_threshold.add_argument("-i", "--invert", action="store_true", default=False,
                                     help="Invert the threshold operation (above cutoff -> black)")

    return parser.parse_args()
