# Marvin Ko – Documentation Process 

This README.md contains the documentation process of what I learned/contributed throughout period of Note Vision.


## Neural Networks Introduction

Watch these videos by *3Blue1Brown* to get a fundamental understanding of what neural networks are and how they work.


### [Chapter 1](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)
---
The video begins by presenting a handwritten digit "three" and marveling at how effortlessly our brains can recognize it, despite variations in pixel values. It introduces the challenge of creating a program that can perform this recognition and sets the stage for explaining neural networks.

It emaphasizes the importance and relevance of machine learning and neural networks. It aims to help viewers understand the structure of neural networks and how they work as a piece of mathematical machinery. The goal is to demystify neural networks and inspire confidence in understanding the concept of "neural network learning."

The focus of this video is primarily on the structure of a neural network. It introduces a simple neural network designed to recognize handwritten digits, with explanations about the layers, neurons, and their role in processing input data.

The video elaborates on neurons, explaining that they are units that hold numbers representing activations between 0 and 1. Neurons in the first layer represent pixel values in an input image, and there are layers of neurons in between (hidden layers) with weights and biases associated with them.

The importance of understanding these layers is discussed, particularly how they might detect edges and patterns, which are building blocks for recognizing digits. The concept of learning in neural networks is introduced, hinting at the process of finding the right values for the weights and biases.

It then transitions to the notation and linear algebra used to represent neural networks, highlighting that a neural network is essentially a complex mathematical function that takes input data and produces an output based on the interactions of weights, biases, and activations.

Learning in a neural network involves adjusting these weights and biases, and the complexity arises from the vast number of parameters (weights and biases) that can be tuned.

The video closes by introducing the ReLU (Rectified Linear Unit) function as an alternative to the sigmoid function, which is commonly used in modern neural networks. This new activation function is explained as being easier to train for deep neural networks.



### [Chapter 2](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)
---
This video provides an overview of neural networks and their learning process. It starts with a recap of the structure of a neural network and then focuses on two main goals. The first goal is to introduce the concept of gradient descent, which is a fundamental part of how neural networks learn. Gradient descent is explained as a method for finding the minimum of a cost function, which helps the network improve its performance on training data.

It emphasizes that the network's learning process involves adjusting the weights and biases of the neurons, which are done through gradient descent. It also touches on the importance of the cost function and its role in evaluating the network's performance.

The video highlights that while this basic neural network structure may not fully capture complex patterns like edges and loops, it's still capable of classifying handwritten digits with decent accuracy. The video suggests that this is just a starting point and that modern neural networks have evolved to perform even better, but understanding this foundational structure is crucial.

Towards the end, the video discusses some recent research papers that explore how deep neural networks learn and address questions about memorization versus generalization in training. These papers shed light on the optimization landscape of neural networks and their ability to find local minima in the cost function.

### [Chapter 3](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)
---
In this video, the presenter discusses backpropagation, which is the core algorithm behind how neural networks learn. The video begins with a recap of neural networks, gradient descent, and the concept of a cost function. The main focus is on providing an intuitive walkthrough of what backpropagation does, without diving into mathematical formulas.

The intuitive walkthrough starts with the idea that for each training example, the network's output is compared to the desired output, and adjustments are made to the network's weights and biases. The adjustments aim to make the network's output closer to the desired output. This process involves considering how sensitive the cost function is to changes in each weight and bias.

The video emphasizes the importance of considering the relative proportions of changes to weights and biases, as some components have a more significant impact on the cost function than others. This approach is somewhat reminiscent of Hebbian theory in neuroscience, where neurons that fire together strengthen their connections.

The presenter explains that backpropagation is the algorithm for determining how a single training example should influence the network's weights and biases. This process is done for all training examples, and the desired changes are averaged to obtain a gradient that guides the network towards minimizing the cost function.

To speed up the computational process, stochastic gradient descent is introduced, which involves randomly dividing the training data into mini-batches for computing gradient updates. This method is more computationally efficient, although it leads to a somewhat "drunken" trajectory towards the cost function's minimum.

In summary, backpropagation is a crucial algorithm for adjusting neural network weights and biases to minimize a cost function. It relies on considering how training examples influence the network's output and requires a large amount of labeled training data to work effectively. Stochastic gradient descent is a practical technique for making the process more efficient.



## PDF -> PNG Converter Script | Python


Designed and implemented a Python script that took in a path to a PDF file as a command line argument that would then convert each page of the PDF file into a series of PNG files that are clustered together into a new directory within the directory.

[Example PDF File](/Users/marvinko/Code/NoteVision/scripts/convertible.pdf)

![Example PNG Image](/Users/marvinko/Code/NoteVision/scripts/pdf2images/page_3.png)

### Prerequisites
---
> Python pdf2image module installation \
> pdf2image installation 
>
>    **Linux**
>>    (1) sudo apt-get install poppler-utils
>>
>>    (2) pip install pdf2image
>
>    **mac** 
>>   (1) brew install poppler 
>>
>>   (2) pip install pdf2image
>>
>    **windows**
>>    (1) conda install -c conda-forge pdf2image
>
> 

## Yolo v5 Instruction
1. git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install



## PyTorch Tutorials

Began watching and learning more about PyTorch through the *Deep Learning with PyTorch: Zero to GANs* series made by the youtuber *Jovian* (parts 1-4 only).

[PyTorch Playlist](https://www.youtube.com/playlist?list=PLyMom0n-MBroupZiLfVSZqK5asX8KfoHL)

### Installation

You can install PyTorch via `pip` according to your system configurations. 

For CPU-only:
```bash
pip install torch torchvision
```

For GPU support (CUDA enabled):
```bash
pip install torch torchvision torchaudio
```


### Getting Started
Importing PyTorch

```python
import torch
import torch.nn as nn
```


### Tensors
The core data structure in PyTorch is a tensor, similar to NumPy's array but with additional GPU acceleration capabilities.


Creating tensors:
```python
# Create an empty tensor
empty_tensor = torch.empty(2, 3)  # Creates a 2x3 uninitialized tensor

# Create a tensor from a Python list
my_list = [1, 2, 3, 4, 5]
tensor_from_list = torch.tensor(my_list)

# Generate a random tensor
random_tensor = torch.rand(3, 2)  # Creates a 3x2 tensor with random values between 0 and 1
```


### Tensor Operations
You can perform various operations on tensors, similar to NumPy arrays.
```python
# Tensor addition
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
result = tensor1 + tensor2

# Matrix multiplication
matrix1 = torch.randn(3, 4)
matrix2 = torch.randn(4, 2)
result_matmul = torch.matmul(matrix1, matrix2)

# Other operations: subtraction, element-wise multiplication, etc.
```


### Autograd and Neural Networks
PyTorch provides a powerful automatic differentiation mechanism through its `autograd` package, which makes training neural networks easier.


Creating a Simple Neural Network
```python
# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # Input size: 10, Output size: 5
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)   # Input size: 5, Output size: 1
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Instantiate the neural network
model = SimpleNN()

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```



### Training a Neural Network
```python
# Example training loop (pseudo-code)
for epoch in range(num_epochs):
    optimizer.zero_grad()  # Zero the gradients
    output = model(input_data)  # Forward pass
    loss = criterion(output, target)  # Calculate loss
    loss.backward()  # Backpropagation
    optimizer.step()  # Update weights
```



## NumPy Basics

### Installation

NumPy is usually installed alongside other scientific computing libraries like SciPy, Matplotlib, etc. If you don't have it installed, you can install it using `pip`:

```bash
pip install numpy
```


### Importing NumPy
To use NumPy, you'll need to import it into your Python environment:

```python
import numpy as np
```


### NumPy Arrays
The core component of NumPy is the `ndarray` (N-dimensional array). It's similar to Python lists, but with added functionalities optimized for numerical operations.

Creating Arrays
You can create NumPy arrays in various ways:


* **From a Python List:**
```python
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
```


* **Using `arange`:**
```python
arr = np.arange(0, 10, 2)  # Creates an array from 0 to 10 (exclusive) with step 2
```

* **With Zeros, Ones, or Empty**
```python
zeros_arr = np.zeros((3, 4))  # Creates a 3x4 array filled with zeros
ones_arr = np.ones((2, 3))    # Creates a 2x3 array filled with ones
empty_arr = np.empty((2, 2))  # Creates a 2x2 empty array (values might be arbitrary)
```

### Array Attributes
NumPy arrays have several attributes that provide information about the array:

* `shape`: Describes the dimensions of the array.
* `dtype`: Specifies the data type of the array elements.
* `ndim`: Indicates the number of dimensions.
* `size`: Represents the total number of elements in the array.

### Array Operations
NumPy allows for efficient mathematical operations on arrays.

* **Element-Wise Operations:**
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition
result_add = arr1 + arr2

# Multiplication
result_mul = arr1 * arr2

# Other operations: subtraction, division, power, etc.
```

* **Array Indexing and Slicing:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing
print(arr[0, 1])  # Accesses element at row 0, column 1

# Slicing
print(arr[1:])    # Retrieves rows starting from index 1 till the end
print(arr[:, 1])  # Retrieves all elements from column 1
```



### Array Functions
NumPy provides various mathematical functions to operate on arrays efficiently.

* **Mathematical Functions:**
```python
arr = np.array([1, 2, 3, 4, 5])

# Sum, mean, standard deviation
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))

# Trigonometric functions, exponential, logarithm, etc.
```










