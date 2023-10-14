# Documentation for Note Vision - Shirley Tom

This documentation contains all of progress on what I have learned during the learning period of the project.

## Video 1 - But what is a neural network? | Chapter 1, Deep learning

This video is the introduction into neural networks. Using the example of an AI learning to read a handwritten letter, the video does a deep dive into how the AI learns to recognize the number. There are layers to the neural network and each layer helps to determine the final number since each layer cooresponds to each component of the number. For example, for number 9, the second layer corresponds to the little edges that create the entire number. Then, those little edges will light up the neurons that corresponds to the loop at the top and the line at the bottom of a 9. Then, this will light up the neuron for the number 9. For each layer of neurons, each neuron in the next layer is connected to all of the neurons from the previous layer. For the connections between the different layers of neurons, there are weights that help detemine whether or not the pixels will generate the number. This is also a bias for each neuron in the second row.

[link to video](https://www.youtube.com/watch?v=aircAruvnKk)

## Video 2 - Gradient descent, how neural networks learn | Chapter 2, Deep learning

This video discusses the concept of gradient descent. 

[link to video](https://www.youtube.com/watch?v=IHZwWFHWa-w)
 
## Python Class Inheritance

To make the child class, you would set the parent class as the parameter. For example, if the parent class was a Fruit, the declaration for the child class would be Berries(Fruit). Any classes that are added to the child class but the parent class has, the parent's function woull be overwritten. There are functions that can be used for certain this. For example, the function super() will be used to inherit all of the properties and methods of the parent class. 

## Dunder methods

Dunder methods are methods that can be used to change the way a class interacts with built in functions and operators. For examples, __init__ and __str__ are two commonly known dunder methods. By adding these dunder methods to a class, the way these functions work can be changed for the class.