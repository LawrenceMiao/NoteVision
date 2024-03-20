import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import io
from PIL import Image
from PIL import ImageOps
from flask import send_file
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

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

    # Store the URL of the inverted image in session storage
    session['inverted_image_url'] = '/' + temp_image_path

    # Redirect to the display page
    return redirect(url_for('display_image'))

@app.route('/display_image')
def display_image():
    # Retrieve the URL of the inverted image from session storage
    inverted_image_url = session.pop('inverted_image_url', None)
    if inverted_image_url:
        return render_template('display_image.html', inverted_image_url=inverted_image_url)
    else:
        # Redirect back to the upload page if no image URL is found
        return redirect(url_for('upload_image'))


def main():
    # given image url, get a request

    return True

