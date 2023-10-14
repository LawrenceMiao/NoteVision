# Documentation - Sophia Chen

This is my progress on Note Vision and everything covered in the course of the semester.

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
<<<<<<< Updated upstream
- The connections can be represented in a notationally compacted way through the matrix vector product with:
    - The activations from one layer are put in a column as a vector
=======
- The connections can be represented in a notationally compact way through the matrix vector product with:
    - The activations from one layer put in a column as a vector
>>>>>>> Stashed changes
    - The weights as a matrix where each row of the matrix shows the connections between one layer and a neuron in the next layer
    - The biases as a vector
    - Adding the bias vector to the previous matrix vector product
    - Apply Sigmoid
- An entire network is basically a function with tons of parameters in the forms of weights and biases that pick up on certain patterns and involve matrix vector products and the sigmoid function

### Chapter 2 - Gradient descent, how neural networks learn

- 

### Chapter 3 - What is backpropagation really doing?

- 

## Python

### Classes

### Files

### NumPy
I learned the basics of NumPy in order to work with arrays to create and plot data sets.

### Pillow
I learned about the different image manipulation techniques such as adding filters like blurring, as well as rotating images and saving images in different file types. The Pillow library can help manipulate multiple images from a folder at once instead of doing it one by one. 

### PyTorch
I touched upon deep learning using the PyTorch framework and learned about how to train a model that goes from producing random noise to fairly good images of handwritten digits and faces.
