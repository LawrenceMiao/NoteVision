# Note Vision | Sherry Lin

Note Vision is an AI tool designed to help enable musicians and composers to transform physical sheet music to a MIDI file.

# Instructions to Install Necessary Environments
Python, Anaconda, Labelme, and Pytorch are necessary for the developement and implementation of NoteVision.

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

## PyTorch
PyTorch is a tensor library for deep learning using GPUs and CPUs.

Before installation, check to make sure you do not already have PyTorch downloaded. To check using Python code, follow the below instructions:

Run Python in your terminal or command prompt.
```
python3
```
Import the torch library, check the PyTorch version:
```
import torch
torch.__version__
```

If there is output and the version is the latest stable version, then you already have PyTorch. However, if you do not follow the instructions: 

1. Create a conda environment named `test_env`
```
conda create --name test_env
```
2. Activate `test_env`
```
conda activate test_env
```
3. Go to this [link](https://pytorch.org/get-started/locally/) and select the following:
  - PyTorch Build: Stable
  - Your OS: _Your OS_
  - Package: Conda
  - Language: Python
  - Compute Platform: Default (if Mac) OR CPU (if Windows/Linux)
4. Copy and paste the command into your environment, and run it.
5. Check that it successfully downloaded by following the instructions from above.

# Introduction to Neural Networks and Deep Learning

## Neural Networks
A network contains multiple neurons that hold information.

### Videos:
- [Chapter 1 | But what is a neural network?](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)
- [Chapter 2 | Gradient descent, how neural networks learn](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)
- [Chapter 3 | What is backpropagation really doing?](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)

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

**Source:** [NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

## Pillow

**Source:** [Python Tutorial: Image Manipulation with Pillow](https://www.youtube.com/watch?v=6Qs3wObeWwc)

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

### Resources:
- [Mask RCNN Guide](https://pytorch.org/vision/main/models/mask_rcnn.html)
- [Mask RCNN GitHub](https://github.com/pytorch/vision/blob/main/torchvision/models/detection/mask_rcnn.py)
- [Test Image Segmentation Dataset](https://www.kaggle.com/datasets/vencerlanz09/plastic-and-paper-cups-synthetic-image-dataset)