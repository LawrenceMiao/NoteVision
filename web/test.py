import os
from flask import Flask, request, render_template
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

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

    if file:
        # Define the folder where you want to save the uploaded files
        upload_folder = 'uploads'

        # Save the file to the specified folder
        file.save(os.path.join(upload_folder, file.filename))

        response = "File uploaded successfully"
    
        # Set CORS headers
        response_headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
        }

        return file.filename, 200

if __name__ == '__main__':
    app.run()
