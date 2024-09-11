from PyPDF4 import PdfFileMerger
import os

# Initialize PdfFileMerger object
merger = PdfFileMerger()

# Iterate over files in the directory
for item in os.listdir():
    if item.endswith('.pdf'):
        merger.append(item)

# Write the merged PDF to a file
with open("Final_pdf.pdf", "wb") as output_pdf:
    merger.write(output_pdf)

# Close the PdfFileMerger object
merger.close()

# Remove individual PDF files
for item in os.listdir():
    if item != 'Final_pdf.pdf' and item.endswith('.pdf'):
        os.remove(item)
