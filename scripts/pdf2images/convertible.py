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

#converts 
def pdf_to_png(input_pdf, output_directory, dpi=200):
    images = convert_from_path(input_pdf, dpi=dpi)

    for i, image in enumerate(images):
        output_path = f"{output_directory}/page_{i + 1}.png"
        image.save(output_path, "PNG")


# generates a new output directory that will store 
# all of the png files that are generated from the pdf
def generate_output_directory(input_directory):
    
    new_directory = str(input_directory).split('/')[-1]
    os.makedirs(new_directory)
    output_directory = os.getcwd() + '/' + new_directory.split(".")[-1]  # Replace with the directory where you want to save the PNG images
    
    return output_directory




if __name__ == "__main__":
    
    
    input_pdf = sys.argv[1]
    output_directory = generate_output_directory(input_pdf)
    
    print(f"input directory: {input_pdf}")
    print(f"output directory: {output_directory}")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print("Converting pdf to png files...")
    pdf_to_png(input_pdf, output_directory)
    print("Sucessfully converted!")


    





