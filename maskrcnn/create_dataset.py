import os, json
from PIL import Image
import numpy as np

def get_indices(patch_size, width, height):
    coors = []
    for i in range((width // patch_size) - 1):
         for j in range((height // patch_size) - 1):
              coors.append([i*patch_size, j*patch_size, (1+i)*patch_size, (1+j)*patch_size])
    return coors

def within_bounds(box1, box2):
    left1, top1, right1, bottom1 = box1
    left2, top2, right2, bottom2 = box2

    # Check if box1 is fully within the bounds of box2
    return left2 <= left1 and top2 <= top1 and right1 <= right2 and bottom1 <= bottom2

def create(img_dir, json_dir):
        os.mkdir("data")
        os.mkdir("data/imgs")
        os.mkdir("data/boxes")
        patch_size = 800
        count = 0
        for file in os.listdir(img_dir):
            if file.split(".")[-2] + ".json" in os.listdir(json_dir):
                img_path = os.path.join(img_dir, file)
                json_path = os.path.join(json_dir, file.split(".")[-2] + ".json")
                with open(json_path, 'r') as json_file:
                    data = json.load(json_file)
                    img_size = (data["imageWidth"], data["imageHeight"])
                    shapes = data["shapes"]
                    img = Image.open(img_path)
                    patch = None
                    
                    coors = get_indices(800, img_size[0], img_size[1])
                    print(coors)
                    for i in coors:
                        boxes = []
                        patch = img.crop(i)
                        for shape in shapes:
                            box_coors = [int(shape["points"][0][0]), int(shape["points"][0][1]), int(shape["points"][1][0]), int(shape["points"][1][1])]
                            if shape["label"] != "notehead":
                                continue
                              
                            if not within_bounds(box_coors, i):
                                continue
                            
                            box_coors = [box_coors[0] - i[0], box_coors[1] - i[1], box_coors[2] - i[0], box_coors[3] - i[1]]
                            boxes.append(box_coors)
                        patch.save(f"data/imgs/patch-{count}.png")
                        np.save(f"data/boxes/patch-{count}.npy", np.array(boxes))
                        count += 1
                            

                                   
                              
                              


create("../dataset/note-labeling/images/cello-sonata", "../dataset/note-labeling/images/cello-sonata-json")