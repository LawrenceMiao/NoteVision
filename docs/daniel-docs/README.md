# *Daniel Shi* – Documentation Process 
This README.md contains the documentation process of what I learned throughout the learning period of Note Vision.


## Neural Networks Introduction:
I watched these videos by *3Blue1Brown* to get a fundamental understanding of what neural networks are and how they work.

##### Video 1 - But what is a neural network? | Chapter 1, Deep learning:
- Neuron: a thing that holds a number between 0 and 1 that represents a greyscale value of a pixel.
    - Closer to 0 for darker pixels.
    - Closer to 1 for lighter pixels.
- A network can be represented as several layers containing the activations of neurons.
- Weights are assigned to each connection between layers to ensure that each pixel generates a valid activation value.
- Activation for each neuron in the following layers after the first one are based on the weighted sum of all neurons in the previous layer plus a special number called a bias.
- Neuron cont.: a function that takes in the outputs of all the neurons in the previous layer and spits out a number between 0 and 1.
- [Link to video](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)

##### Video 2 - Gradient descent, how neural networks learn | Chapter 2, Deep learning:
- Gradient descent can be used to calculate which weights and biases minimize a certain cost function.
- To calculate the cost of the network for every training example you square the difference between the network's output with your desired output and take the average.
- This will allow you to find the negative gradient of the cost function which tells you how to adjust all the weights and biases to efficiently decrease the cost.
- [Link to video](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)

##### Video 3 - What is backpropagation really doing? | Chapter 3, Deep learning:
- Three different ways to increase an activation:
    - Increase bias.
    - Increase weights propotional to the activations from previous layer.
    - Change activations from previous layer proportional to the size of the corresponding weights.
- Backpropagation moves backwards through the network to recursively adjust relevant weights and biases
- [Link to video](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)

## PyTorch Notes:
I read documentation on how to use PyTorch so I that could apply what I learned about neural networks