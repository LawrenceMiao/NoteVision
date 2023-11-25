import os
from flask import Flask, request, render_template, send_file
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('../music/submit.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('../music/submit.html')
    elif request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        if file:
            # Define the folder where you want to save the uploaded files
            upload_folder = 'uploads'

            # Save the file to the specified folder
            file_path = (os.path.join(upload_folder, file.filename))
            file.save(file_path)

            return send_file(file_path, mimetype='image/*')

if __name__ == '__main__':
    app.run()
