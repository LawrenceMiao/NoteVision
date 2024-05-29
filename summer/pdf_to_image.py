from pdf2image import convert_from_path
from PIL import Image


def pdf_to_image(pathname: str) -> list[Image.Image]:
    return convert_from_path(pathname)
