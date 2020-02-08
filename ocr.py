"""Evaluate OCR quality"""

import os
import PyPDF2
from random import seed, randint

seed(42)

root = "data/bn/"
#root = "data/nbn/"

for fn in sorted(os.listdir(root)):
    filename = root+fn
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    nb_pages = pdf_reader.numPages
    n = randint(10, nb_pages-1)
    page_obj = pdf_reader.getPage(n)
    text = page_obj.extractText()
    with open(f"data/ocr/raw/{fn[:-4]}_{n}.txt", "w") as output:
        output.write(text)
