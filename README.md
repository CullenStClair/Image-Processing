
# Python Image Processing CLI

[![CI Test Suite](https://github.com/CullenStClair/Image-Processing/actions/workflows/run-tests.yml/badge.svg)](https://github.com/CullenStClair/Image-Processing/actions/workflows/run-tests.yml)

A command line interface for performing image processing tasks.  
Built as a personal project with the purpose of learning and using NumPy.

## Features

- Supports reading and writing most common image formats
- Provides optional settings for tweaking certain operations
- Supported Operations:
  - Box Blurring
  - Chain (Queue Multiple Operations)
  - [To Do] Compositing (Alpha Blending)
  - Convolving (With a Custom Kernel)
  - Cropping
  - Edge Detection
  - Grayscaling
  - Inverting Colours
  - Mirroring (Horizontal and Vertical)
  - Rotating (Clockwise and Counterclockwise)
  - [To Do] Sepia Toning
  - Sharpening (Unsharp Masking)
  - Thresholding (Colour or Black and White)

## Set Up Locally

Clone the project

```bash
  git clone https://github.com/CullenStClair/Image-Processing.git
```

Go to the project directory "Image-Processing"

```bash
  cd Image-Processing
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Usage

List all available operations

```bash
  python main.py --help
```

Show usage and details for a given operation

```bash
  python main.py <in-file-path> <out-file-name> <operation> --help
```

### Example

Rotate `C:\Downloads\logo.png` by 180 degrees and save as `C:\Downloads\flipped.png`

```bash
  python main.py "C:\Downloads\logo.png" flipped.png rotateCW --turns 2
```

You may also use relative file paths, for example:  `tests/logo.png`  
The output file is saved in the same directory as the input file.

`C:\Downloads\logo.png`  |  `C:\Downloads\flipped.png`
:-------------------------:|:-------------------------:
![Original Logo Image](https://i.imgur.com/cKBXnKi.png) | ![Flipped Logo Image](https://i.imgur.com/OBnyQbF.png)

## License and Reuse

Copyright (C) 2023  Cullen St-Clair  
Licensed under the GNU GPL v3.0 License.  
Take a look at the [LICENSE](https://github.com/CullenStClair/Image-Processing/blob/master/LICENSE) file for detailed information.

## Contributing

Since this is a personal project, please do not submit pull requests.  
Thanks for checking it out!
