# Note Vision Documentation - Sophia Chen

Note Vision is a tool for musicians and composers to easily convert picture(s) of physical handwritten sheet music to digial MIDI files using AI. 

## Installation Guides
There are a few packages and softwares that are required for this project including Anaconda, PyTorch, and LabelMe. 


### Anaconda
There are two installation options: Anaconda and Miniconda. It is highly recommended to install Anaconda although it is a much larger package. 

Follow the instructions to install Anaconda or Miniconda on:
- [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)

After installation, you can test the package by going to your terminal window or Anaconda Prompt and running the command:

```
conda list
```

A list of installed packages will appear if the installation was successfull. 

### PyTorch
To install the PyTorch library locally for your operating system, first head over to the [PyTorch website](https://pytorch.org/get-started/locally/). Open up your terminal window and create and activate a new conda environment by running the commands:

```
conda create --name test_env
conda activiate test_env
```

From the website, select the following: Stable (2.1.0), Windows, Conda, Python, CPU. If you use the Linux or Mac OS, select that instead of Windows. Note that for Windows users, PyTorch only supports Windows 7 or greater. 

Copy and run the generated command after making the selections in your terminal window or command prompt.

To check if the installation was successful, run the following Python script:

```
import torch
print(torch.__version__)
```

### LabelMe


## Neural Networks and Deep Learning

### Chapter 1 - But what is a neural network?

- The task is to put together a neural network that can learn to recognize handwritten digits
- Multilayer perceptron is the simplest variant of a neural network, yet it can still recognize handwritten digits.
- Network starts with neurons corresponding to pixels of an input image
- Each neuron holds a number holding a grayscale value; ranging from 0 for black pixels to 1 for white pixels and is lit up when the activation is a high number
- The activation in the neuron represents how much the system thinks the given image corresponds to a given digit
- The activation in one layer determines the activation in the next layer
- The brightest neuron of the output layer is the network's choice for what digit the image represents
- The goal is to have some mechanism that could combine pixels into edges into patterns into digits
- There is a weight assigned to each connection from one neuron to another
- The weighted sum of the pixel values would give us the region of pixels that we care about 
- Negative weights would help indicate where the edges are since they would be darker
- The Sigmoid function helps condense the weighted sums into the range between 0 and 1
- Negative inputs end up close to zero while positive inputs end up close to 1
- The activation of a neuron is a measure of how positive the weighted sum is
- We add a bias to the calculation of the weighted sum to tell how high the weighted sum needs to be to be meaningfully active
- Each connection between neurons has its own weight and bias associated with it
- The connections can be represented in a notationally compacted way through the matrix vector product with:
    - The activations from one layer are put in a column as a vector
- The connections can be represented in a notationally compact way through the matrix vector product with:
    - The activations from one layer are put in a column as a vector
    - The weights as a matrix where each row of the matrix shows the connections between one layer and a neuron in the next layer
    - The biases as a vector
    - Adding the bias vector to the previous matrix vector product
    - Apply Sigmoid
- An entire network is basically a function with tons of parameters in the forms of weights and biases that pick up on certain patterns and involve matrix vector products and the sigmoid function

### Chapter 2 - Gradient descent, how neural networks learn

- An example of how a layered structure of a network learns goes like this:
    - The first layer takes in images of handwritten numbers that are to be deciphered
    - The second layer picks up on the edges 
    - The third layer picks up on patterns like loops and lines 
    - The last layer pieces pieces together the patterns to recognize digits
- A large amount of training data is provided to a network to train it to see how well it can classify images
- A cost function takes in the weights and the biases and outputs a single number (the cost) through many training examples which measures how lousy a network is
- The algorithm for computing the gradients efficiently is called backpropagation.
- 

### Chapter 3 - What is backpropagation really doing?

- 

## Python

### Classes

### Files

## NumPy
I learned the basics of NumPy in order to work with arrays to create and plot data sets.

## Pillow
The Python Imaging Library is a free and open-source library for the Python and C language that helps with opening, manipulating, processing, and saving different image file formats. Some image manipulation techniques the library offers include adding filters, blurring objects and people, and rotating images. The Pillow library can help manipulate multiple images from a folder at once instead of doing it individually as well, which makes it really useful. The library is available to install for Windows, MAC OS X, and Linux.

## PyTorch
I touched upon deep learning using the PyTorch framework and learned how to train a model that goes from producing random noise to fairly good images of handwritten digits and faces.

## Mask R-CNN
Mask R-CNN stands for Mask Region-based Convolutional Neural Network and is a deep learning instance segmentation technique where pixel-level segmentation is performed on the objects. After images get passed in the layers in the neural network, the loss is computed. This loss is how different the predicted results are from the actual expected results. The training process includes looking at the loss, adjusting the weights, and recalculating the outputs using the original images as input. The cycle continues with numerous iterations until the final CNN, the AL model used for predictions. 

