import glob
import os
import shutil
from pathlib import Path

import numpy as np
from PIL import ExifTags
from tqdm import tqdm

# Parameters
img_formats = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng']  # acceptable image suffixes
vid_formats = ['mov', 'avi', 'mp4', 'mpg', 'mpeg', 'm4v', 'wmv', 'mkv']  # acceptable video suffixes

# Get orientation exif tag
for orientation in ExifTags.TAGS.keys():
    if ExifTags.TAGS[orientation] == 'Orientation':
        break


def exif_size(img):
    # Returns exif-corrected PIL size
    s = img.size  # (width, height)
    try:
        rotation = dict(img._getexif().items())[orientation]
        if rotation in [6, 8]:  # rotation 270
            s = (s[1], s[0])
    except:
        pass

    return s


def split_rows_simple(file='../data/sm4/out.txt'):  # from utils import *; split_rows_simple()
    # splits one textfile into 3 smaller ones based upon train, test, val ratios
    with open(file) as f:
        lines = f.readlines()

    s = Path(file).suffix
    lines = sorted(list(filter(lambda x: len(x) > 0, lines)))
    i, j, k = split_indices(lines, train=0.9, test=0.1, validate=0.0)
    for k, v in {'train': i, 'test': j, 'val': k}.items():  # key, value pairs
        if v.any():
            new_file = file.replace(s, f'_{k}{s}')
            with open(new_file, 'w') as f:
                f.writelines([lines[i] for i in v])


def split_files(out_path, file_name, prefix_path=''):  # split training data
    file_name = list(filter(lambda x: len(x) > 0, file_name))
    file_name = sorted(file_name)
    i, j, k = split_indices(file_name, train=0.9, test=0.1, validate=0.0)
    datasets = {'train': i, 'test': j, 'val': k}
    for key, item in datasets.items():
        if item.any():
            with open(f'{out_path}_{key}.txt', 'a') as file:
                for i in item:
                    file.write('%s%s\n' % (prefix_path, file_name[i]))


def split_indices(x, train=0.9, test=0.1, validate=0.0, shuffle=True):  # split training data
    n = len(x)
    v = np.arange(n)
    if shuffle:
        np.random.shuffle(v)

    i = round(n * train)  # train
    j = round(n * test) + i  # test
    k = round(n * validate) + j  # validate
    return v[:i], v[i:j], v[j:k]  # return indices


def make_dirs(dir='new_dir/'):
    # Create folders
    dir = Path(dir)
    if dir.exists():
        shutil.rmtree(dir)  # delete dir
    for p in dir, dir / 'labels', dir / 'images':
        p.mkdir(parents=True, exist_ok=True)  # make dir
    return dir


def write_data_data(fname='data.data', nc=80):
    # write darknet *.data file
    lines = ['classes = %g\n' % nc,
             'train =../out/data_train.txt\n',
             'valid =../out/data_test.txt\n',
             'names =../out/data.names\n',
             'backup = backup/\n',
             'eval = coco\n']

    with open(fname, 'a') as f:
        f.writelines(lines)


def image_folder2file(folder='images/'):  # from utils import *; image_folder2file()
    # write a txt file listing all imaged in folder
    s = glob.glob(f'{folder}*.*')
    with open(f'{folder[:-1]}.txt', 'w') as file:
        for l in s:
            file.write(l + '\n')  # write image list


def add_coco_background(path='../data/sm4/', n=1000):  # from utils import *; add_coco_background()
    # add coco background to sm4 in outb.txt
    p = f'{path}background'
    if os.path.exists(p):
        shutil.rmtree(p)  # delete output folder
    os.makedirs(p)  # make new output folder

    # copy images
    for image in glob.glob('../coco/images/train2014/*.*')[:n]:
        os.system(f'cp {image} {p}')

    # add to outb.txt and make train, test.txt files
    f = f'{path}out.txt'
    fb = f'{path}outb.txt'
    os.system(f'cp {f} {fb}')
    with open(fb, 'a') as file:
        file.writelines(i + '\n' for i in glob.glob(f'{p}/*.*'))
    split_rows_simple(file=fb)


def create_single_class_dataset(path='../data/sm3'):  # from utils import *; create_single_class_dataset('../data/sm3/')
    # creates a single-class version of an existing dataset
    os.system(f'mkdir {path}_1cls')