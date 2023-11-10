# *Daniel Shi* – Documentation Process 
This README.md contains the documentation process of what is required for Note Vision.


## Neural Networks Introduction
I watched these videos by *3Blue1Brown* to get a fundamental understanding of what neural networks are and how they work.

##### Video 1 - But what is a neural network? | Chapter 1, Deep learning
Link to video: (https://www.youtube.com/watch?v=aircAruvnKk)
- Neuron: a thing that holds a number between 0 and 1 that represents a greyscale value of a pixel.
    - Closer to 0 for darker pixels.
    - Closer to 1 for lighter pixels.
- A network can be represented as several layers containing the activations of neurons.
- Weights are assigned to each connection between layers to ensure that each pixel generates a valid activation value.
- Activation for each neuron in the following layers after the first one are based on the weighted sum of all neurons in the previous layer plus a special number called a bias.
- Neuron cont.: a function that takes in the outputs of all the neurons in the previous layer and spits out a number between 0 and 1.

##### Video 2 - Gradient descent, how neural networks learn | Chapter 2, Deep learning
Link to video: https://www.youtube.com/watch?v=IHZwWFHWa-w
- Gradient descent can be used to calculate which weights and biases minimize a certain cost function.
- To calculate the cost of the network for every training example you square the difference between the network's output with your desired output and take the average.
- This will allow you to find the negative gradient of the cost function which tells you how to adjust all the weights and biases to efficiently decrease the cost.

##### Video 3 - What is backpropagation really doing? | Chapter 3, Deep learning
Link to video: (https://www.youtube.com/watch?v=Ilg3gGewQ5U)
- Three different ways to increase an activation:
    - Increase bias.
    - Increase weights propotional to the activations from previous layer.
    - Change activations from previous layer proportional to the size of the corresponding weights.
- Backpropagation moves backwards through the network to recursively adjust relevant weights and biases

## PyTorch

##### Installation

In order to get started with PyTorch you must have Anaconda installed. To install Anaconda visit the Anaconda website: https://www.anaconda.com/products/distribution. Here you will select the version best suited for your operating system and download the installer. After opening the installer, follow the basic setup wizard to completion.

Once Anaconda is installed visit the PyTorch website: https://pytorch.org/get-started/locally/. On this page you will find a table of preferences. Select the preferences based on your operating system to aqquire the correct install command. Copy the provided install command.

Open command prompt and create a new environment. In the command prompt enter the line:
conda create --name (environment name) (version of python). After doing so activate the new environment and paste the install commmand and follow the provided instructions.

##### Pytorch Information

- useful functions:
    - torch.rand(tuple representing its size) -> intitialize a tensor with values between 0 and 1
    - torch.ones(tuple representing its size) -> intitialize a tensor with 1 as values 
    - torch.zeros(tuple representing its size) -> intitialize a tensor with 0 as values
    - tensor_name.shape -> returns the size of the tensor
    - torch.cat([tensors], dimensions) -> concatenate a sequence of tensors along a given dimension
- indexing/slicing:
    - tensor[0] -> refers to the first row
    - tensor[:, 0] -> refers to the first column
    - tensor[..., -1] -> refers to the last column
    - tensor[:,1] -> alter the second column
- for one-element tensors it is possible to sum up all values into a one value using:
    - total = tensor_name.sum()
    - total_item = total.item()
- in-place operations are denoted by a "_" suffix:
    - Ex: tensor_name.add_(5)

---

PyTorch provides two data classes: torch.utils.data.Dataset and torch.utils.data.DataLoader. These classes allow users to use pre-loaded datasets as well as their own data. the Dataset stores the samples and their corresponding labels, and DataLoader wraps an iterable around the Dataset to make accessing samples easier. For more information on creating custom datasets visit the link: https://pytorch.org/tutorials/beginner/basics/data_tutorial.html

---

Neural network models are all subclasses of nn.Module as it is the base class for all neural network modules. Here is an example of initializing a neural network:

class NeuralNetwork(nn.Module):  
    
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

To learn about what each class within the neural network does visit the link: https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html

---

As mentioned earlier neural networks utilize back propagation which depends on weights that are determined by the gradient of the loss function with respect to the given weight. PyTorch contains a built-in called torch.autograd that automatically computes these gradients. There are two ways to use this built-in: (1) When initialing a new tensor set the parameter requires_grad to true [Ex: torch.randn(5, 3, requires_grad=True)]. (2) With an already existing tensor you can do x.requires_grad_(True). Where x represents the tensor. requires-grad allows the gradients for that tensor to be calculated. To actually access the gradients you would add .grad to the end of the variable containing your tensor, but before doing so you would include the line t.backward() once if working with a single graph. Where t represents the lost function. For more information on gradient tracking visit the link: https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html

---