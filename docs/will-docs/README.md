will
Chapter 1 - But what is a neural network?
What are neurons?
Neurons is a node that holds a value called activation values
Neurons hold values and are activiated depending on a situtation/the inputs               < The individual
                                                                                          | activations are
How do layers work?                                                                       | nothing but together
Activations of neurons in one layer determines what gets activiated in the next layer     | they can "recognize"
|                                                                                         | circumstances.
V                                                                                         |
How does one layer affect another layer?                                                  |
A neuron network is trained and in the circumastances in the enviroment in one layer determines
how the next layer is activiated.

Why do layers work?
Our brain recognizes parts of a number and pices them to make a number

Neurons in layers can represent parts of the number. From the first layer which each node represents 
a pixel and the activiation of each pixel to the parts of the number and each layer with in a way
comes closer to determining a full number.

How neurons are lit up?
Ex: While observing a reigon seeing n what pixels are lit up will determine the edge the is recongized
in the following layer. 

The combinations of neuron activiation will activitate neurons in the next layer.

How does the math function?
Ex: Assigning a weight to each connection.

Neuron activation = weight * activation + bias

-1 -.5 -.5 -.5 -.5  -1
 1   2   2   2   2   1
 1   2   2   2   2   1

 The reigon above shows a part of a image and the weights and bias associated to each pixel for a neuron in the next layer. Meaning if the activation of neurons is high in the row that the weights are negative those neurons will negatively impact the activation of the neuron in the next layer. So you want the neurons in the negative
 row to not be activated and the activation of the positive rows to be high so it would be more likely the neuron
 in the next layer is activated. Of course values of 2 are greater than 1 so the neurons that have the higher 
 weights are more important.

 We want activations to be 0 < x < 1
 We use the sigmoid function. Negative # are closer to zero and vice versa

 More in the math?
 The weights associated to the neurons determines if activation will benefit or negatively impact the activation
 of the neuron it is connected to.

 What does the bias do?
 It helps determine when the activation of the neuron is important or not? Despite the 
 weight * activation_Val being positive like 5 and the sigmoid function determines the output by convering it to a 
 value from 0 to 1 and in that case 1. The bias is added to the weight*activtationP_val before it gets converted by the sigmoid function and determines how much 
 that value matters before converting it into the sigmoid function. So if you want the weight*activation value to be greater than 10 before that value becomes 
 significant the bias sorta says nope that value needs to be greater than 10 before it matters so if the value before the bias is 5 with the bias added on it 
 it says the current activation is not enough. THe bias determines the y intercept and offests the graph. 
 
 sigmoid function((w1*a1 -10) + (w2*a2 - 10) ... (wn*an - 10))

 Chapter 2 - Gradient descent and analyzing a network

 How does the network learn and what do we want?
 We want an algo that takes in a bunch of training data which is a bunch of labeled images.
 The algo will adjust the weights and biases and improve the performance on the training data.
 The layered structure will hopefully allow the neural network to have decent performance on other
 new training sets. 

Note: We will understand that machine learning will feel like calculus.
This is because we neural network is basically optimizing a function to find the miniumums

 Neural networks learn:
 First initalize the neural network with random weights and biases. The network will do 
 horribily at first

 The cost function we then define will tell the computer what it's doing bad. The cost function
 compares the outputs with the output we want.

 Example: The output the network gave has activations for neurons 1,6, 7 ,8 ,9 when we want
 and output with only an activation for 3 and low to no activation for other neurons.

 Mathematically: 
 Add up the squares of the differences between the trash activation and the activation we want

 summation of (every_computer_output - correspoding_desired_output)^2 = cost of training example
 The sum is small when the network is confident gets the desired output and vice versa.
 We consider the average cost of all the training examples. That value determines how accurate
 and how bad the computer should feel about the performance.

 Remember: The network is a function that has inputs and spits out an output. Then it is parametrize 
 by the weights and biases (Parameters: #weights, #bias)

 The cost function is added complexity. Takes in as input 13002 weights/bias and outputs 1 number(cost)
 and the parameters are the many training examples.

 Telling the computer that the performance is bad isn't helpful so how can we improve the growth mindset.

 We are then trying to minimize the cost function because we want the lowest cost value possible.

 For the function start at a random input and then find the slope to slowly find local minimum which is doable.
 However we want the global min which is crazy difficult.

 Taking the slope and adjusting the step size portionately to the slope will make the step size smallers as we approach the 
 minimum.

 Further away from the min will often result in a steeper slope which means the step should be larger.