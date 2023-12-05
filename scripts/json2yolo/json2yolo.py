import json
import os
from pathlib import Path

import requests
import yaml
from PIL import Image
from tqdm import tqdm


def convert(file, zip=True):
    # Convert Labelbox JSON labels to YOLO labels
    names = []  # class names
    file = Path(file)
    save_dir = make_dirs(file.stem)
    with open(file) as f:
        data = json.load(f)  # load JSON