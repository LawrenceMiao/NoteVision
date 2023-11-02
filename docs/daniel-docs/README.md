# *Daniel Shi* – Documentation Process 
This README.md contains the documentation process of what is required for Note Vision.


## Neural Networks Introduction

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

In order to get started with PyTorch you must have Anaconda installed. To install Anaconda visit the Anaconda website: https://www.anaconda.com/products/distribution. Here you will select the version best suited for your operating system and download the installer. After opening the installer, follow the basic setup wizard to completion.

Once Anaconda is installed visit the PyTorch website: https://pytorch.org/get-started/locally/. On this page you will find a table of preferences. Select the preferences based on your operating system to aqquire the correct install command. Copy the provided install command.

Open command prompt and create a new environment.In the command prompt enter the line:
conda create --name (environment name) (version of python). After doing so activate the new environment and paste the install commmand and follow the provided instructions.