# Note Vision Documentation - Sherry Lin
 This file documents my learning process and my contributions while working on NoteVision.

Note Vision is an AI tool designed to help enable musicians and composers to transform physical sheet music to a MIDI file.

## Introduction to Neural Networks and Deep Learning

I watched the following three videos by *3Blue1Brown* to get an understanding of what neural networks are, how they work, and what backpropagation is in order to better comprehend how deep learning works.

- [Chapter 1 | But what is a neural network?](https://youtu.be/aircAruvnKk?si=bKe3I8pQEtDHPTxS)
- [Chapter 2 | Gradient descent, how neural networks learn](https://youtu.be/IHZwWFHWa-w?si=bdLgCjGBCk_S1ENU)
- [Chapter 3 | What is backpropagation really doing?](https://youtu.be/Ilg3gGewQ5U?si=7DkytDDaGr3OIsuv)

Some key points are:

- Neural networks contain neurons which can activate in layers to determine a final answer.
- The cost of the network allows it to calculate the negative gradient in order for proper learning.
- Backpropagation is the algorithm for computing the gradient descent.

## Expanding Python Knowledge

I explored multiple sources listed below to learn more about Python that Computer Science 1 did not cover. Topics include classes,  dunder methods, file handling, NumPy, and Pillow. 

- [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [Dunder Methods](https://mathspp.com/blog/pydonts/dunder-methods)
- [File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python File Open](https://www.w3schools.com/python/python_file_open.asp)
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
- [Python Delete File](https://www.w3schools.com/python/python_file_remove.asp)
- [NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)
- [Python Tutorial: Image Manipulation with Pillow](https://www.youtube.com/watch?v=6Qs3wObeWwc)

I learned that:

- Python inheritance allows programmers to create child clases that inherit methods and properties from parent classes and allows child classes to override inherited methods. 
- Dunder methods let class objects interact with built-in functions, keywords, and operators of Python. g
- Python provides various handling functions including "open()", ".read()", ".readline()", ".close()", ".write()", ".remove()", and more. 
- NumPy is a Python library used for working with ar
rays and matrices and includes high-level mathematical functions.
- Pillow is a Python library that lets programmers work with and manipulate images.

## Mask R-CNN Model
Mask R-CNN, Mask Region-based Convulation Neural Network, is a deep learning model used for image segmentation and object detection. Image segmentation is a type of object detection that generates a segmentation map for each detected instance of an object and treats individual objects as distinct entities, regardless of the class of the object. The general steps for transfer learning for Mask R-CNN are as follows: 
1. Configure using the `maskrcnn` object.
2. Prepare training data.
3. Train using the trainMaskRCNN function.
4. Evaluate using the `evaluateInstanceSegmentation` function.

### Sources:
- [What is Mask R-CNN? The Ultimate Guide](https://blog.roboflow.com/mask-rcnn/)
- [Mask RCNN GitHub](https://github.com/matterport/Mask_RCNN)
- [Everything about Mask R-CNN: A Beginner’s Guide](https://viso.ai/deep-learning/mask-r-cnn/)
- [Getting Started with Mask R-CNN for Instance Segmentation](https://www.mathworks.com/help/vision/ug/getting-started-with-mask-r-cnn-for-instance-segmentation.html)

## JSON Parser Python Script
I developed and implemented a Python script that took in a path to a JSON file as the first command line argument and an optional second argument that would be the output file name. The script would parse the JSON file, remove the image attribute, and output to a new file that is by default named "[original filename]_clean.json" or the optional second argument.

## Test Model

[Test Image Segmentation Dataset](https://www.kaggle.com/datasets/vencerlanz09/plastic-and-paper-cups-synthetic-image-dataset)
