
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
  python src/main.py -h
```

Show arguments for a given operation

```bash
  python src/main.py <in-file-path> <out-file-name> <operation> -h
```

Example: Crop `/img-editor/tests/images/logo.png` to within corners (100, 100) and (300, 300)

```bash
  python src/main.py tests/images/logo.png out.png crop 100 100 300 300
```

You may also use absolute file paths, for example:  `"C:\...\logo.png"`  
Output file is saved in the same directory as the input file.

Input: `/tests/images/logo.png`
![/pics/logo.png](https://i.imgur.com/Yhkyi1G.png)

Output `/tests/images/out.png`

![/pics/out.png](https://i.imgur.com/1W2HwAN.png)

## Contributing

Since this is a personal showcase project, I kindly ask that you do not submit pull requests.  
If you try the program and would like to report a bug, you are welcome to open an issue, but please do not use this to suggest features.  

## License and Reuse

Copyright (C) 2023  Cullen St-Clair  

Take a look at the [LICENSE](https://github.com/CullenStClair/img-editor/blob/master/LICENSE) file.

## Acknowledgements

Test images graciously provided by [Pexels](https://www.pexels.com/).  
Please see the [ATTRIBUTIONS](https://github.com/CullenStClair/img-editor/blob/master/ATTRIBUTIONS.md) file.
