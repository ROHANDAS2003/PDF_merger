# PDF Merger

## Overview

**PDF Merger** is a Python script that merges multiple PDF files into a single PDF document using the PyPDF4 library. The script automatically merges PDFs in the same folder and deletes the individual files afterward.

## Features

- Merges multiple PDF files into a single output file.
- Simple and easy-to-use command-line interface.
- Automatically deletes the original PDF files after merging.

## Prerequisites

- **Python**: Ensure Python is installed. Check your version by running:

<<<<<<< HEAD
=======

>>>>>>> ad5bef68ab1107163474ad22c1a108e635c0402a
python --version

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

- **PyPDF4**: Install the PyPDF4 library, which handles the PDF merging:


pip install PyPDF4

If you're using Python 3, the command might be:

<<<<<<< HEAD
=======

>>>>>>> ad5bef68ab1107163474ad22c1a108e635c0402a
pip3 install PyPDF4

## How to Clone and Use the Project

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

<<<<<<< HEAD
git clone https://github.com/ROHANDAS2003/PDF_merger
=======

git clone [PDF_merger](https://github.com/ROHANDAS2003/PDF_merger)


cd PDF_merger

>>>>>>> ad5bef68ab1107163474ad22c1a108e635c0402a

### Step 2: Set Up the Folder Structure

Ensure your PDF files are in the same directory as the pdf_merger.py script. For example:

<<<<<<< HEAD
=======


>>>>>>> ad5bef68ab1107163474ad22c1a108e635c0402a
project-folder/

├── pdf_merger.py
├── document1.pdf
├── document2.pdf
└── document3.pdf


### Step 3: Install Dependencies

Make sure the required dependencies are installed by running the following command:

pip install PyPDF4

If you're using Python 3, you might need to run:

pip3 install PyPDF4


### Step 4: Run the Script

Now that the PDF files are in the same directory and dependencies are installed, you can run the script. Make sure you're still in the project directory and run:

python pdf_merger.py

For Python 3, run:

python3 pdf_merger.py


### Step 5: Output

The script will create a merged PDF file named Final_pdf.pdf in the same directory. After merging, the individual PDF files will be deleted, and the folder will contain only the merged output:

project-folder/

└── Final_pdf.pdf

## Commands Summary

\# Clone the repository

git clone https://github.com/ROHANDAS2003/PDF_merger


\# Navigate into the project folder

cd folder-name


\# Install PyPDF4 dependency

pip install PyPDF4 # or pip3 install PyPDF4


\# Run the script to merge PDFs

python pdf_merger.py # or python3 pdf_merger.py


## Limitations

- This script only merges PDF files located in the same directory as the script.
- It does not handle encrypted or corrupted PDF files.

## Future Enhancements

- Add support for merging PDFs from different directories.
- Option to specify a custom output file name.
- Improved error handling for corrupted or encrypted PDF files.

By following these instructions, you will be able to successfully clone, set up, and run the PDF Merger script. If you encounter any issues, feel free to reach out via GitHub.
