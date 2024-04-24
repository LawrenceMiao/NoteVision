import os
from flask import Flask, request, render_template, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import jsonify
import torch
import cv2
import numpy as np


app = Flask(__name__)
CORS(app)

# Define the upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Function to ensure the upload folder exists
def ensure_upload_folder():
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])


@app.route("/")
def index():
    return render_template("music/submit.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    ensure_upload_folder()  # Ensure the upload folder exists

    # Save the file to the specified folder with the original filename
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
    )
    file.save(file_path)

    return secure_filename(file.filename)


# Route to serve uploaded files
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# Route to handle model requests
@app.route("/predict", methods=["POST"])
def predict():
    # obtain image
    image_data = request.json.get("image")

    # load model

    # Preprocess the image data
    image = torch.as_tensor(image, dtype=torch.float32)
    image = image.permute(2, 0, 1)  # Change the order of dimensions
    image.unsqueeze(0)  # Add batch dimension

    # Load the model
    model = load_model()

    # Perform inference
    with torch.no_grad():
        model.eval()
        predictions = model(preprocessed_image)

    # format predicitions
    
    # return the prediction as JSON response
    return jsonify({"prediction": prediction})


# placeholder function for model
def model_inference(image_data):
    return "Model prediction"


if __name__ == "__main__":
    app.run(port=5000)
