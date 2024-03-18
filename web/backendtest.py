import requests
from flask import Flask, request, jsonify
import io
from PIL import Image
from PIL import ImageOps
from flask import send_file

app = Flask(__name__)

# check

@app.route('/invert_image', methods=['POST'])
def invert_image():
    # Check if the request contains an image
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    # Read the image file from the request
    image_file = request.files['image']
    
    # Read the image as a PIL Image object
    image = Image.open(io.BytesIO(image_file.read()))

    # Invert the image
    inverted_image = ImageOps.invert(image)

    # Save the inverted image to a temporary file
    temp_image_path = 'static/inverted_image.jpg'
    inverted_image.save(temp_image_path, format='JPEG')

    # Return the URL of the inverted image
    return '/' + temp_image_path



def main():
    # given image url, get a request

    return True

