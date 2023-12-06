# Note Vision Documentation - Sophia Chen

Note Vision is a tool for musicians and composers to easily convert pictures of physical handwritten sheet musics to digial MIDI files using AI. 

## Installation Guides
There are a few packages and softwares that are required for this project including Python, Anaconda, PyTorch, and LabelMe. 

### Python

To check if you have Python installed, first open your terminal window or command prompt. 

For Windows users, run:

```
py --version
```

For Mac users, run: 

```
python3 --version
```

If Python is installed, you should see a message like this:

```
Python 3.11.5
```

If Python is not installed, download the appropriate package on the [Python website](https://www.python.org/downloads/windows/).


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

From the website, select the following: Stable (2.1.0), Windows, Conda, Python, CPU. If you use the Linux or Mac OS, select that instead of Windows. Note that for Windows users, PyTorch only supports Windows 7 or greater. 

Copy and run the generated command after making the selections in your terminal window or command prompt.

## Neural Networks and Deep Learning

The main objective of neural networks is to create a system that is capable of learning and recognizing handwritten digits. This begins with a multilayer perceptron, the simplest variant of a neural network. This network represents an input image with a large group of neurons where each neuron corresponds to a pixel in the image. Each neuron encapsulates a grayscale value, ranging from 0 (representing black pixels) to 1 (representing white pixels). Neurons activate based on their grayscale values and how much a system believes the given image corresponds to a specific digit. The activation in one layer influences the activation in the subsequent layer, ending in the brightest neuron of the output layer representing the network's chosen digit. 

To detect patterns, the network assigns weights to connections between neurons. These weights are crucial in distinguishing the relevant pixels. Negative weights are beneficial for representing the presence of edges as they correspond to darker areas in the image. The Sigmoid function is used to transform the weighted sum of the pixel values into a manageable range. The function condenses the sums into the range between 0 and 1, with negative inputs tending toward 0 and positive inputs towards 1.

In addition to weights, biases play a key role in the calculation of the weighted sums. Biases determine when a neuron becomes active. Each neuron connection includes its weight and bias, contributing to the behavior of the network. 

To efficiently represent connections within the network, matrix vector products are used: 

- Activations from one layer are organized as a column vector
- Weights are arranged as a matrix, with each row signifying connections between one layer and a subsequent layer's neuron
- Biases are represented as a vector

Matrix vector multiplication with the addition of the bias vector provides the input for the Sigmoid function. 

In essence, a neural network is a complex mathematical function, full of parameters in the form of weights and biases. These parameters play a vital role in recognizing patterns within the input data. As the network processes information through matrix vector products and applies the Sigmoid function, it becomes an adaptable tool to be used for numerous tasks.

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

## Pillow
The Python Imaging Library is a free and open-source library for the Python and C language that helps with opening, manipulating, processing, and saving different image file formats. Some image manipulation techniques the library offers include adding filters, blurring objects and people, and rotating images. The Pillow library can help manipulate multiple images from a folder at once instead of doing it individually as well, which makes it really useful. The library is available to install for Windows, MAC OS X, and Linux.

## PyTorch
I touched upon deep learning using the PyTorch framework and learned how to train a model that goes from producing random noise to fairly good images of handwritten digits and faces.

## Mask R-CNN
Mask R-CNN stands for Mask Region-based Convolutional Neural Network and is a deep learning instance segmentation technique where pixel-level segmentation is performed on the objects. After images get passed in the layers in the neural network, the loss is computed. This loss is how different the predicted results are from the actual expected results. The training process includes looking at the loss, adjusting the weights, and recalculating the outputs using the original images as input. The cycle continues with numerous iterations until the final CNN, the AL model used for predictions. 

