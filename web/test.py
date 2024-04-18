import os
from flask import Flask, request, render_template, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to ensure the upload folder exists
def ensure_upload_folder():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('music/submit.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    ensure_upload_folder()  # Ensure the upload folder exists

    # Save the file to the specified folder with the original filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(file_path)

    return "File uploaded successfully"


if __name__ == '__main__':
    app.run(port=5000)
