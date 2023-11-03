# Note Vision | Sherry Lin

Note Vision is an AI tool designed to help enable musicians and composers to transform physical sheet music to a MIDI file.

# Instructions to Install Necessary Environments
Python, Anaconda, Labelme, and Pytorch are necessary to the developement of NoteVision.

## Anaconda
Download the appropriate version of [Anaconda](https://www.anaconda.com/download) for your device or follow the appropriate installation guides below making sure to follow Anaconda instructions.

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
To run LabelMe in macOS, run `labelme` in the terminal. In the context of NoteVision, LabelMe was used to annotate sheet music and the annotations were saved as a JSON file. The JSON file was run through the JSON parser Python Script in order to remove unnecessary image attributes.

## PyTorch

# Introduction to Neural Networks and Deep Learning

## Neural Networks
A network contains multiple neurons that hold information. 

- [Chapter 1 | But what is a neural network?](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)
- [Chapter 2 | Gradient descent, how neural networks learn](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)
- [Chapter 3 | What is backpropagation really doing?](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)

# Relevant Python Information

## Python Classes and Inheritance
Python inheritance allows programmers to create child clases that inherit methods and properties from parent classes and allows child classes to override inherited methods.

- [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [Dunder Methods](https://mathspp.com/blog/pydonts/dunder-methods)

## Python File Handling

- [File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python File Open](https://www.w3schools.com/python/python_file_open.asp)
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
- [Python Delete File](https://www.w3schools.com/python/python_file_remove.asp)

## NumPy

- [NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)

## Pillow

- [Python Tutorial: Image Manipulation with Pillow](https://www.youtube.com/watch?v=6Qs3wObeWwc)

