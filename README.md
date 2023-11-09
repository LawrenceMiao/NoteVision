# NoteVision

## About

## Dependency Installation

### Anaconda
There are two installation options: Anaconda and Miniconda. It is highly recommended to install Anaconda although it is a much larger package. 

Follow the instructions to install Anaconda or Miniconda on:
- [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
- [Linux]() *issue - linux installation instructions*

### Anaconda Environment Setup (Pytorch)
*issue - anaconda environment setup for pytorch*
Follow the instructions below to setup PyTorch in a conda environment: 

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
5. Check that it successfully downloaded by following the instructions below.

Using Python code, follow the below instructions:

Run Python in your terminal or command prompt.
```
python3
```
Import the torch library, check the PyTorch version:
```
import torch
torch.__version__
```

If there is output and the version is the latest stable version, then you have successfully installed PyTorch in a conda environment.

### Labelme
*issue - labelme installation instructions*

