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

## Python Classes and Inheritance
Python inheritance allows programmers to create child classes (base classes) that inherit methods and properties from parent classes (derived classes). Any class can be a parent class, but to create a child class that inherits from another class, you need to make the parent class a parameter of the child class.

### Sources:
- [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [Dunder Methods](https://mathspp.com/blog/pydonts/dunder-methods)

## Python File Handling
Python

### Sources:
- [File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python File Open](https://www.w3schools.com/python/python_file_open.asp)
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
- [Python Delete File](https://www.w3schools.com/python/python_file_remove.asp)

## NumPy
Python

**Source:** [NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

## Pillow
Python

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