import matplotlib.pyplot as plt # for plotting
import numpy as np # for transformation

import torch # PyTorch package
import torchvision # load datasets
import torchvision.transforms as transforms # transform data
import torch.nn as nn # basic building block for neural neteorks
import torch.nn.functional as F # import convolution functions like Relu
import torch.optim as optim # optimzer

def imshow(img):
    ''' function to show image '''
    img = img / 2 + 0.5 # unnormalize
    npImg = img.numpy() # convert to numpy objects
    plt.imshow(np.transpose(npImg, (1, 2, 0)))
    plt.show()

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == '__main__':
    # Initialize model
    model = Model()

    # Initialize optimizer
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    # Print model's state_dict
    print("Model's state_dict:")
    for paramTensor in model.state_dict():
        print(paramTensor, "\t", model.state_dict()[paramTensor].size())

    # Print optimizer's state_dict
    print("Optimizer's state_dict:")
    for varName in optimizer.state_dict():
        print(varName, "\t", optimizer.state_dict()[varName])

    # torch.save(model.state_dict(), "model.pt")

    loadedModel = Model()
    loadedModel.load_state_dict(torch.load("model.pt"))
    loadedModel.eval()

    for i in loadedModel.parameters():
        print(i)