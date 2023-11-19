# Note Vision | Sherry Lin

Note Vision is an AI tool designed to help enable musicians and composers to transform physical sheet music to a MIDI file.

# Instructions to Install Necessary Environments and Libraries
Python, PIP, Anaconda, Labelme, Pytorch, NumPy, Pillow, and OpenCV are necessary for the development and implementation of NoteVision.

## Python
Python often comes pre-installed, so check if your device has Python or which version of Python it runs by running the following code:
```
python -version

# run if there is an error for the prior command
python3 –version
```
If both commands fail, then you likely do not have Python and need to download Python 3.

If the version number is Python 2.x.y, where x and y are unknown numbers, you will need to update to Python 3 because Python 2.x.y is no longer supported and is not recommended for development.

Head to https://www.python.org/downloads/ and download the appropriate OS version of Python, and run the command above again to make sure you have the latest version of Python 3.

**Source:** https://wiki.python.org/moin/BeginnersGuide/Download

## Anaconda
Download the appropriate version of [Anaconda](https://www.anaconda.com/download) for your device or follow the appropriate installation guides below. (Note: make sure to follow the Anaconda specific instructions.)

- [Windows installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [macOS installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
- [Linux installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

## PIP
If you have Python version 3.4 or later, PIP is included by default. However, if you do not have PIP, head to this [link](https://pip.pypa.io/en/stable/installation/) and follow the instructions. 

## LabelMe
LabelMe is a image annotation tool that lets users annotate images and export the annotations as a JSON file.

Follow this [link](https://github.com/wkentaro/labelme) for LabelMe installation. The instructions are simplified below:

### Anaconda
Run code below in Anaconda Prompt:
```
conda create --name=labelme python=3
source activate labelme
pip install labelme
```

### Ubuntu
```
sudo apt-get install labelme
```

### macOS
```
brew install pyqt  
pip install labelme
```

### Windows
Run code below in Anaconda Prompt:
```
conda create --name=labelme python=3
conda activate labelme
pip install labelme
```

### App
Install app from: https://github.com/wkentaro/labelme/releases

### Run and Use LabelMe 
To run LabelMe in macOS, run `labelme` in the terminal. In the context of NoteVision, LabelMe is used to annotate sheet music and the annotations are saved as a JSON file. The JSON file is then run through the JSON parser Python script in order to remove unnecessary image attributes.

## NumPy
Anaconda is a Python distribution that already has NumPy installed but if you want to install NumPy anyway then using Python and PIP, run the following command:
```
pip install numpy
```

## Pillow
If you need to install Pillow, you can install it with PIP and Python:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
You can find more specific instructions [here](https://pillow.readthedocs.io/en/stable/installation.html).

## OpenCV
To install OpenCV in the `test_env` conda environment, run the following commands:
```
conda activate test_env
pip install opencv-python
```

# Introduction to Neural Networks and Deep Learning
Note: An example problem that will be used for this section is training a model to recognize handwritten digits from 0 to 9.

## Neural Networks
In biology, neural networks or neural circuit are groups of neurons that are functionally or chemically connected. Each individual neuron can be connected to many other neurons. When the biological neural circuit is activited a specific function is carried out. Biological neural circuits inspired artificial neural networks. 

An artifical neural network or just neural network contains multiple neurons that hold information. Each neuron may be connected to many other neurons similar to the neural circuits. Each connection or edge can transmit signals to other neurons. The articial neuron recieves signals, processes them, then sends signals to other neurons. The signal is a number that can be used to compute some weighted sum or other function. Neurons and edges have weights to them that adjust the more the model learns. The purpose of the weight is to increase or decrease the strength of a signal of an edge. They usually have thresholds where only when the neuron crosses the threshold will a signal be sent.

Usually, neurons are aggregated into multiple layers. The layers help detect edges and patterns that help determine what the image is a digit of. Each layer can perform different transformations to their input. Signals travel from the first layer which usually has hundreds of neurons to the last layer where an answer is chosen. The signals often travel through multiple layers in order to get from the first to the last layer. 

<!-- example -->

Following the example, each neuron would hold a number between 0 and 1 which is the greyscale value of the corresponding pixel given an image of a handwritten digit. Specifically, black pixels are represented as 0 and white pixels are denoted as 1. 

There are around seven hundred eighty four neurons that make up the first layer and just ten neurons in the last layer that represent the digits. There are hidden layers between the first and last layer that signals get sent through. To get to the last layer, certain groups of neurons fire which cause certain other groups to fire and eventually the signal reaches the last layer. This layered structure essentially helps the model narrow down what the digit is through testing. 

However, there needs to be a way to combine pixels into edges, edges into patterns, patterns into digits. This is done with weights and weighted sum. Weights are assigned to each one of the edges between the neuron and the neurons from the first layer. By taking the weighted sum of all the pixels amounts to the sum of pixel values that matter. To improve edge detection of a digit, incorporate negative weights. Through negative weights, the sum is largest when the pixels are bright and the surrounding pixels are dark. 

This weighted sum needs to be between 0 and 1 for activation, so it is best to use some function that squishes any input into a number between 0 and 1. A common function that achieves this is the sigmoid function that basically simplifies to very negative inputs are close to 0 and very positive inputs are close to 1. In order to make sure a weight is significant, there should be a bias. The weights indicates what pixel pattern is seen by a layer and the bias indicates how high the weighted sum needs to be to be significant. There are thousands of weights and biases and part of the learning is to tweak each weight and bias. However, tweaking every single weight and bias individually would take a lot of time and effort, so the AI model is responsible for learning what to change. 

## Gradient Descent

Gradient descent is used to help train machine learning models and neural networks. Backpropagation is the efficient algorithm for computing the gradient descent. The cost function within gradient descent is an instrument that gauges accuracy every iteration of parameter updates. The model will adjust its parameters until it yiels the smallest possible error. The purpose of gradient descent is to minimize the cost function and in order to do this, it needs two things: direction and learning rate. These determine the partial derivative calculations of future iterations, allowing it to gradually arrive at a local or global minimum. There are multiple types of gradient descent like stochastic, batch, etc. 

There are many issues with using gradient descent for optimization. Some of the problems include local mimima, saddles points, and vanishing and exploding gradients. Gradient descent can easily find global minimum in convex problems but struggles to in nonconvex problems because it stops learning when the slope is close or at zero. Vanishing gradients are gradients that are too small. As the model moves towards backpropagation, the gradient gradually becomes smaller causing earlier layers to learn more slowly. The weight parameters update until they are insignificant which results in an algorithm that is no longer learning. Exploding gradients occur when the gradient is too large which results in an unstable model. The weight parameters become too large where they will be represented as NaN. However, gradient descent is still good for helping ML models learn. 

### Sources:
- [Chapter 1 | But what is a neural network?](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)
- [Chapter 2 | Gradient descent, how neural networks learn](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)
- [Chapter 3 | What is backpropagation really doing?](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)
- [What is gradient descent?](https://www.ibm.com/topics/gradient-descent)

# Relevant Python Information

## Python Classes
### Inheritance
Python inheritance allows programmers to create child classes (base classes) that inherit methods and properties from parent classes (derived classes). Any class can be a parent class, but to create a child class that inherits from another class, you need to make the parent class a parameter of the child class. 

If your child class does not need any other methods or properties, use the `pass` keyword so that the class simply inherits everything. However, if you want to alter parts of the child class, do not use `pass` and create your own methods where you can call the parent class methods either using the parent class's name or `super()`. If you add a method with the same name as a method in the parent class, the inheritance of the parent method will be overridden. 

For example, you can add the `__init__()` function to the child class which overrides the parent class's `__init__()` function. The `__init__()` function is automatically called every time an instance of the class is created. In the new `__init__()` function, you can call the parent `__init__()` function by using either the name or `super()`.

### Super()
The `super()` function is used to refer to the parent class. It is a normal practice in object-oriented programming to inherit from parent classes and allow for method override. You can enhance the usability of the parent class without altering it. The benefits of using `super()` include: 
- It is not necessary to remember the name of the parent class even in single or multiple inheritances
- It is dynamic which allows you to change the structure of classes at run-time unlike static programming languages.
- It implements modularity which is isolating changes so the original code remains intact and code reusability because you do not have to rewrite the entire function. 

### Dunder Methods
Dunder methods, also known as magic methods, let class objects interact with built-in functions, keywords, and operators of a language in this case Python. The names of dunder methods usually begin and end with two underscores which is where the name, dunder, came from. Dunder methods are not typically directly called by the programmer rather they are called implicitly.

A well-known dunder method is the `__init__()` function which is in charge of initializing instances of your class. It is rarely called directly instead runs automatically. 

There is no special reason for the two underscores at the beginning and end of the method name and regular functions created by programmers can also begin and end with two underscores. The purpose of the two underscores is to prevent name collision with functions programmers may create. For example, there is a `__sum__()` dunder method but programmers often create their own `sum` functions, so if the dunder method did not have the underscores then you accidentally lose access to the built-in function by overriding the original dunder method.

All Python operators rely on dunder methods to execute their behavior which is why it does not matter that some names of dunder methods like `__sum__()` are inconvenient to use because they are rarely called explicitly. You can overload certain operators to make them work customly with your class objects by implementing the respective dunder method that corresponds to the operator.

There are many dunder methods, you can find a list of many of them [here](https://mathspp.com/blog/pydonts/dunder-methods#list-of-dunder-methods-and-their-interactions).

### Sources:
- [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [Python Super()](https://www.geeksforgeeks.org/python-super/)
- [Dunder Methods](https://mathspp.com/blog/pydonts/dunder-methods)

## Python File Handling
Python provides various functions for file handling. A key function is the `open()` function which takes in two parameters: the file name and mode. If the file is located in a different location than the Python code, then the file name needs to include the file path. There are four different modes for opening the file:
- "r": The read mode opens the file for reading, raises an error if the file does not exist, and is one of two default values when `open()` is called.
- "w": The write mode opens the file for writing and if the file does not exist, creates the file.
- "a": The append mode opens the file for appending and if the file does not exist, creates the file.
- "x": The create mode creates the file and raises an error if the file already exists.
You can specify what way the file should be handled by adding either of the following to the mode.
- "t": Text mode is one of two default values when `open()` is called.
- "b": Binary mode
The `open()` function returns a file object which has a  `read()` method so you can read the content of the file. 

The `read()` method returns the entire text of the file by default, but you can choose how many characters you want to return by putting a number in the parenthesis of `read()`. You can use `readline()` to return a single line of the file. You can call `readline()` multiple times, and it will return a new line if there is one every time. You can read the entire file, line by line, if you loop through the lines using `readline()`.

There are two modes to write to existing files: "w" and "a". The "w" mode will overwrite the entire file.

You should always close a file when you are done with it by using `close()` and some changes made to files may not show up until the file is closed.

You must import the OS module and run the `os.remove()` function in order to delete a file. However, you want to check if the file exists before deleting it to avoid getting any errors. You can use `os.path.exists()` to check if the file exists. In addition, you can delete a folder, using the `os.rmdir()` function, but you can only delete empty folders.

### Sources:
- [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python Read Files](https://www.w3schools.com/python/python_file_open.asp)
- [Python Write/Create Files](https://www.w3schools.com/python/python_file_write.asp)
- [Python Delete Files](https://www.w3schools.com/python/python_file_remove.asp)

## NumPy
NumPy, "Numerical Python," is a Python library used for working with arrays and has functions for linear algebra, fourier transform, and matrices. NumPy attempts to provide an array object that is much faster than tradition Python lists. The array object is called `array` and NumPy provides many supporting functions that make working with the array object quite easy. NumPy arrays are faster than lists because they are stored in one place in memory unlike lists.

You can import NumPy into your applications with `import numpy as np`. The `as` keyword imports NumPy under an alias, `np`, which lets you use the package as `np` now.

There are many different functions NumPy contains and you can learn more by visiting the link below. 

**Source:** [NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

## Pillow
Pillow is a Python library used to manipulate and modify images. Pillow is built on top of PIL, Python Image Library, and is a fork for it since PIL was discontinued in 2021. It will allow you to do many things to images like cropping, resizing, altering the colors, and more. You can modify many images at once or run a script that automatically changes any images that are uploaded to a certain directory. Pillow supports many image formats including JPEG, PNG, TIFF, and more. 

You can import Pillow into your applications with `from PIL import Image`.

You can read and display the image using `open()` and `show()`. To display the image, Pillow converts the image to PNG format, stores it temporarily, and then displays it. However, the image conversion is not lossless, so some properties might be gone. So, it is advised to only use this method for test purposes.

Each image has a `.size`, `.format`, and `.mode` attributes. The size attribute returns the image size in a tuple that contains the width and height. The format attribute returns the image file format. The mode attribute returns the type and depth of the pixel in the image. There are many different modes provided by Pillow.

You can rotate the image using the `rotate()` method. After image rotation, any sections of the image that have no pixel values are filled with black for non-alpha images or with transparent pixels for images that support transparency.

The `transpose()` method of the Image class can be used to transpose the image. You can flip or rotate the image in ninety degree steps. There are two keywords that can be passed to the transpose method:
- FLIP_TOP_BOTTOM: Returns the given image vertically flipped
- FLIP_LEFT_RIGHT: Returns the given image horizontally flipped

You can resize an image with the `resize()` method. The quality changes depending on whether the image is resized to bigger or smaller, so this method should be used cautiously.

The `save()` method saves the image using the given filename. If the format is unspecified, the format to use it determined from the filename extension. You do not have to use a filename and can use a file object instead in which case you must specify the format and it must implement the seek, tell, and write methods. In addition, it must be opened in binary mode.

There are many more complex operations not listed here. You can find them by looking through the Pillow documentation.

### Sources: 
- [Python Tutorial: Image Manipulation with Pillow](https://www.youtube.com/watch?v=6Qs3wObeWwc)
- [Python Pillow Tutorial](https://www.geeksforgeeks.org/python-pillow-tutorial/)
# HTTP

## What is HTTP

HTTP is a protocol that fetches resources like HTML documents, JSON data, images, and more. It is the foundation for any exchange of data on the Web and is a client-server protocol. The requests are initiated by the recipient which is usually a Web browser. Clients and servers communicate by exchanging individual messages, the messages sent by the client are __requests__ and the server messages are __responses__. HTTP can be used to fetch videos, post content to servers, and parts of documents to update pages. 

Usually the client is a Web browser, but it can be anything. Each request is sent to a server. Between the server and client there are many parts that perform different operations and act as caches before a response is sent back. There are more computers between a browser and server like modems, routers, etc. The Web is layered so those computers and parts are hidden in the network and transport layer. HTTP is the application layer and is on top of the rest. 

The client, also known as the user-agent, is any tool that acts on behalf of users. The user-agent is always the entitiy initiating requests. To display a Web page, the user-agent sends a request to fetch the HTML document, parses the file, makes additional requests, lays out information to show, and resources contained in the page. The user-agent combines all these resources to present a completed document: the Web page. 

The standard file format for creating and presenting a Web page is a hypertext document or HTML. Some parts of the displayed content are links which can be activated to fetch new Web pages. This allows users to direct their user-agent and navigate through the Web. 

A server may be a collection of servers that share load or other software that may partially or totally generate HTML on demand. A server is not always a single machine but several isntances on the same machine. They could even share the same IP address. 

Between a server and a Web browser, there are many computers and machines that are relaying HTTP messages due to the layered design of the Web. Most of those computers and machines operate at the network, transport, or physical levels. Proxies operate on the application layers and can perform many functions like caching, filtering, authicating, logging, and load balancing. 

HTTP is designed to be simple and readable which provides easier testing to developers. New functionality can be introduced easily with HTTP headers. HTTP cookies allow for stateful using header extensibility as HTTP is stateless. The cookies let each HTTP request share the same state. Connections are out of scope for HTTP but it only requires the connection to be reliable . The two most common transport protocols are TCP and UDP. TCP is more reliable and therefore is the standard usually. 

## HTTP Flow
When an user-agent wants to communicate with a server, the following steps occur:
1. Open a TCP connection
2. Send an HTTP message
3. Read the server response
4. Close or reuse the connection
Several requests can be sent if HTTP pipelining is activated. 

## HTTP Messages
There are two kinds of messages: requests, responses. A request consists of an HTTP method, resource path, HTTP protocol version, optional headers, and a body. The HTTP method could be `GET`, `POST`, `OPTIONS`, etc. HTTP methods are explored more in depth below. A response consists of HTTP protocol version, status code, status message, headers, and an optional body.

## HTTP Request Methods
HTTP has a set of __request methods__ that indicate desired actions to be performed for given resources. Request methods can be safe, cacheable, or idempotent. An HTTP request method is safe if the state of the server is unchanged. It is idempotent if the indented effect on the server for one request is the same as making several identical requests. All safe methods are idempotent. A response is cacheable if it can be stored to be restrieved and used later also known as cached. Some methods are listed below:
- `GET`: The `GET` method requests the specified resource's representation.
- `POST`: The `POST` method submits an entity to th specified resource which usually causes a change in state or affects the server.
- `DELETE`: The `DELETE` method deletes the specified resource.

### Sources:
- [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

# Mask R-CNN Model
A CNN is a type of artificial neural network that is used in image recognition and processing optimized for pixel data. The CNN Architecture consists of three main layers:
- Convolutional layer
- Pooling layer
- Fully connected layer

Mask R-CNN, Mask Region-based Convolutional Neural Network, is a deep learning model used for pixel-wise image segmentation and object detection. Image segmentation is a type of object detection that generates a segmentation map for each detected instance of an object and treats individual objects as distinct entities, regardless of the class of the object. The general steps for transfer learning for Mask R-CNN are as follows: 
1. Configure using the `maskrcnn` object.
2. Prepare training data.
3. Train using the trainMaskRCNN function.
4. Evaluate using the `evaluateInstanceSegmentation` function.

The backbone for a Mask R-CNN model is usually a pre-trained CNN. The backbone extracts high-level information and processes images. Mask R-CNN is a powerful model for various computer vision tasks like object detection, image segmentation, and multi-object segmentation. However, it has limitations that include:
- Computational complexity 
- Data requirements
- Small-object segmentation

### Sources:
- [What is Mask R-CNN? The Ultimate Guide](https://blog.roboflow.com/mask-rcnn/)
- [Everything about Mask R-CNN: A Beginner’s Guide](https://viso.ai/deep-learning/mask-r-cnn/)
- [Getting Started with Mask R-CNN for Instance Segmentation](https://www.mathworks.com/help/vision/ug/getting-started-with-mask-r-cnn-for-instance-segmentation.html)

# Test Model

<!-- not done -->

### Resources:
- [Mask RCNN Guide](https://pytorch.org/vision/main/models/mask_rcnn.html)
- [PyTorch Mask RCNN GitHub](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/mask_rcnn.py)
- [Okery PyTorch Simple Mask RCNN GitHub](https://github.com/Okery/PyTorch-Simple-MaskRCNN)
- [multimodallearning Mask RCNN GitHub](https://github.com/multimodallearning/pytorch-mask-rcnn)
- [Test Image Segmentation Dataset](https://www.kaggle.com/datasets/vencerlanz09/plastic-and-paper-cups-synthetic-image-dataset)
- [Fine-tune PyTorch Pre-trained Mask-RCNN](https://haochen23.github.io/2020/06/fine-tune-mask-rcnn-pytorch.html)