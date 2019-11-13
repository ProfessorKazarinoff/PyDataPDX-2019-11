# convert_slides.py
"""
A Python script to convert a multi-page PDF to a directory of images
Uses the pdf2image package
"""

from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

images = convert_from_path('PeterKazarinoff_PyDataPDX_2019-11.pdf')

for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
