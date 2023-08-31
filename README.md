# PDF Watermarker App

The PDF Watermarker App is a Python application that enables you to add a watermark to existing PDF files. This graphical user interface (GUI) tool is built using the `PyPDF2` library for PDF manipulation and the `tkinter` library for creating the user interface.

![PDF Watermarker Screenshot](screenshot.png)

## Features

- Load a template PDF file that you want to watermark.
- Load a watermark PDF file that will be added as a watermark to the template.
- Generate a new PDF file with the watermark applied to each page of the template.
- Easy-to-use graphical user interface.

## Prerequisites

- Python 3.x
- `PyPDF2` library
- `tkinter` library (usually comes with Python)

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

## Usage

1. Run the application by executing the `watermark.py` script:
   ```shell
   python main.py
   ```
2. The application window will appear.
3. Follow the on-screen instructions to perform the following steps:
   - Select a template PDF file by clicking the "Browse" button next to "Select Template PDF."
   - Select a watermark PDF file by clicking the "Browse" button next to "Select Watermark PDF."
   - Click the "Watermark PDF" button to generate the watermarked PDF file.
4. The watermarked PDF file will be saved in the same directory as the `main.py` script.

## Screenshots

You can find screenshots of the application in the `screenshots` directory.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

