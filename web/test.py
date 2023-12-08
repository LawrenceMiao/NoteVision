import os
from flask import Flask, request, render_template, send_file
from flask_cors import CORS
from torch import nn
import torch



app = Flask(__name__)
CORS(app)


# PyTorch Neural Network
class TestModelV0(nn.Module):
  def __init__(self, input_shape: int, hidden_units: int, output_shape: int) -> None:
    super().__init__()
    self.conv_block_1 = nn.Sequential(
        nn.Conv2d(in_channels=input_shape,
                  out_channels=hidden_units,
                  kernel_size=3,
                  stride=1,
                  padding=1),
        nn.BatchNorm2d(num_features=hidden_units),
        nn.ReLU(),
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  stride=1,
                  padding=1),
        nn.BatchNorm2d(num_features=hidden_units),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,
                     stride=2), # Default stride value is same as kernel size
    )
    self.conv_block_2 = nn.Sequential(
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  stride=1,
                  padding=1),
        nn.BatchNorm2d(num_features=hidden_units),
        nn.ReLU(),
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  stride=1,
                  padding=1),
        nn.BatchNorm2d(num_features=hidden_units),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,
                     stride=2), # Default stride value is same as kernel size
    )
    self.classifier = nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features=hidden_units*16*16,
                  out_features=output_shape)
    )


  def forward(self, x):
    return self.classifier(self.conv_block_2(self.conv_block_1(x)))


# Load in all the classes and its respective dictionary
allClasses = []
classDict = {}
model_0 = QuickDrawModelV0(input_shape=1, hidden_units=10, output_shape=len(allClasses))
model_0.load_state_dict(torch.load('model.pth'))
model_0.eval()


# Transform the image
data_transform = transforms.Compose([
    transforms.Resize(size=(64, 64)),
    transforms.Grayscale(1),
    transforms.ToTensor()
])

# Function to make prediction
def make_predictions(model: torch.nn.Module, data, device: torch.device = "cpu"):
    pred_probs = []
    model.eval()
    with torch.inference_mode():
        # Prepare sample
        sample = torch.unsqueeze(data, dim=0).to("cpu") # Add an extra dimension and send sample to device

        # Forward pass (model outputs raw logit)
        pred_logit = model(sample)

        # Get prediction probability (logit -> prediction probability)
        pred_prob = torch.softmax(pred_logit.squeeze(), dim=0)

        # Get pred_prob off GPU for further calculations
        pred_probs.append(pred_prob.cpu())

    # Stack the pred_probs to turn list into a tensor
    return torch.stack(pred_probs)
  

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
