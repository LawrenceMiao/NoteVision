# Documentation for Note Vision - Shirley Tom

This documentation contains information on all of the technologies used on Note Vision.

## Video 1 - But what is a neural network? | Chapter 1, Deep learning

This video is the introduction into neural networks. Using the example of an AI learning to read a handwritten letter, the video does a deep dive into how the AI learns to recognize the number. There are layers to the neural network and each layer helps to determine the final number since each layer cooresponds to each component of the number. For example, for number 9, the second layer corresponds to the little edges that create the entire number. Then, those little edges will light up the neurons that corresponds to the loop at the top and the line at the bottom of a 9. Then, this will light up the neuron for the number 9. For each layer of neurons, each neuron in the next layer is connected to all of the neurons from the previous layer. For the connections between the different layers of neurons, there are weights that help detemine whether or not the pixels will generate the number. This is also a bias for each neuron in the second row.

[link to video](https://www.youtube.com/watch?v=aircAruvnKk)

## Video 2 - Gradient descent, how neural networks learn | Chapter 2, Deep learning

This video discusses the concept of gradient descent. 

[link to video](https://www.youtube.com/watch?v=IHZwWFHWa-w)

## Video 3 - What is backpropagation really doing? | Chapter 3, Deep learning

This video is about 

[link to video](https://www.youtube.com/watch?v=Ilg3gGewQ5U)

## Python Class Inheritance

Python class inheritance is used when you want a class to inherit the methods and variables from another class. There are two components in python inheritance
	- the parent class: the class that is being inherited from
	- the child class: the class that will be inheriting the methods and variables

For this example, we will be using the following class as our parent class.
```py
class Fruit: 
	def __init__(self, newName, newSeason):
		self.name = newName
		self.season = newSeason
	
	def printInfo(self):
		print("I am a {} and I am harvested during the {}.", self.name, self.season)
```

In order to declare a child class, the parent class will be set as a parameter. If we don't want to add any new functions to child class, we can just put pass as shown below.
```py
class Citrus(Fruit): 
	pass
```

The following code shows another way to declare a child class. This child class will have the same `__init__` function as the parent by specifying putting the parent class before the `__init__` function. However, the `printInfo()` function of the child will override the `printInfo()` function of the parent.
```py
class Berry(Fruit): 
	def __init__(self, newName, newSeason):
		Fruit.__init__(self, newName, newSeason)
	
	def printInfo(self):
		print("I am a type of berry called {}. I am harvested during the {}.", self.name, self.season)
```

To inherit all of the methods and variables from the parent class is to use `super()` in front of the `__init__` function. In the following child class, you can see how to add additional methods and variables to the child class. 
```py
class Melon(Fruit): 
	def __init__(self, newName, newSeason, newColor):
		super().__init__(self, newName, newSeason)
		self.color = newColor
	
	def printMoreInfo(self):
		print("I am a {}. I am harvested during the {}. I am a(n) {} melon, which means I have grow on a vine and contain many seeds.", self.name, self.season, self.color)
```

- [inferitance info](https://www.w3schools.com/python/python_inheritance.asp)
- [more info](https://www.geeksforgeeks.org/inheritance-in-python/)

## Dunder methods

Dunder methods are methods that can be used to change the way a class interacts with built in functions and operators. For examples, __init__ and __str__ are two commonly known dunder methods. By adding these dunder methods to a class, the way these functions work can be changed for the class.


## PyTorch

Using PyTorch, we can fine tune Mask RCNN on a custom dataset. Mask RCNN is a deep learning instance segmenetation technique that is used to detected objects. To design a Mask RCNN network, you need to specify the classs and anchor boxes. There are two stages to a Mask RCNN network. The first stage is a regional proposal network. It will create bounding boxes based on anchor boxes. The second stage is a RCNN detector that fine tunes the bounding boxes. To train a Mask RCNN, you need three things aside from the image: the ground-truth bounding boxes, instances labels, and instance masks. All four items will be needed in order to train the Mask RCNN. 

[link to video](https://www.youtube.com/watch?v=vV9L71hK-RE)
[link to article](https://www.mathworks.com/help/vision/ug/getting-started-with-mask-r-cnn-for-instance-segmentation.html)