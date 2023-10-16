'''
pdf2image installation 

# linux
(1) sudo apt-get install poppler-utils
(2) pip install pdf2image

# mac
(1) brew install poppler
(2) pip install pdf2image

# windows
(1) conda install -c conda-forge pdf2image
'''

from pdf2image import convert_from_path
import os, sys


def pdf_to_png(input_pdf, output_directory, dpi=200):
    images = convert_from_path(input_pdf, dpi=dpi)

    for i, image in enumerate(images):
        output_path = f"{output_directory}/page_{i + 1}.png"
        image.save(output_path, "PNG")
        print(f"Page {i + 1} saved as {output_path}")



if __name__ == "__main__":
    
    
    input_pdf = sys.argv[1]
    new_directory = "pdf2images"
    os.makedirs(new_directory)
    output_directory = os.getcwd() + '/' + new_directory  # Replace with the directory where you want to save the PNG images

    print(f"input directory: {input_pdf}")
    print(f"output directory: {output_directory}")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print("Converting pdf to png files...")
    pdf_to_png(input_pdf, output_directory)
    print("Sucessfully converted!")


    





