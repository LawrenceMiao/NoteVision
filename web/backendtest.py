import requests
from flask import Flask, request, jsonify
import io
from PIL import Image

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

    # Convert the inverted image back to bytes
    inverted_image_bytes = io.BytesIO()
    inverted_image.save(inverted_image_bytes, format='JPEG')
    inverted_image_bytes.seek(0)

    # Send the inverted image back to the client
    return send_file(inverted_image_bytes, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)



def main():
    # given image url, get a request

    return True

