from pdf_to_image import pdf_to_image
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    images = pdf_to_image(filename)
