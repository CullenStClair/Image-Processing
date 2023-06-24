
# Python Image Editor

A command line interface for performing image processing tasks.  
Built as a personal project with the purpose of learning and using NumPy.

## Features

- Supports reading and writing most common image formats
- Provides optional settings for tweaking certain operations
- Common image processing operations:
  - Box Blurring
  - Cropping
  - Grayscaling
  - Inverting Colours
  - Mirroring (Horizontal and Vertical)
  - Resizing (Scaling)
  - Rotating (Clockwise and Counterclockwise)
  - Sepia Toning
  - Sharpening
- Advanced image processing operations:
  - Chain (Queue Multiple Operations)
  - Compositing (Alpha Blending)
  - Concatenating
  - Convolving (With a Custom Kernel)
  - Edge Detection
  - Thresholding (Binary Segmentation)

## Set Up Locally

Clone the project

```bash
  git clone https://github.com/CullenStClair/img-editor
```

Go to the project directory "img-editor"

```bash
  cd img-editor
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

Example: Rotate `D:\Downloads\logo.png` by 180 degrees and save as `flipped.png`

```bash
  python main.py "D:\Downloads\small.png" flipped.png rotateCW --turns 2
```

You may also use relative file paths, for example:  `tests/logo.png`  
Output file is saved in the same directory as the input file.

`D:\Downloads\logo.png`  |  `D:\Downloads\flipped.png`
:-------------------------:|:-------------------------:
![Original Logo Image](https://i.imgur.com/cKBXnKi.png) | ![Flipped Logo Image](https://i.imgur.com/OBnyQbF.png)

## License and Reuse

Copyright (C) 2023  Cullen St-Clair  
Licensed under the GNU GPL v3.0 License.  
Take a look at the [LICENSE](https://github.com/CullenStClair/img-editor/blob/master/LICENSE) file for detailed information.

## Contributing

Since this is a personal project, please do not submit pull requests.  
If you try the program and would like to report a bug, you are welcome to open an issue.
