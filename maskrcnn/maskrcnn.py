import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision.models.detection import MaskRCNN_ResNet50_FPN_Weights
from torchvision.models.detection import faster_rcnn
import cv2
import random
import os
import numpy as np
from PIL import Image
import json

def load_dataset(img_path, json_path, mask_path=None):
    pass

class yourmom:
    def __init__(self, img_dir, json_dir, patch_dim: (int, int, int), mask_path=None):
        self.pages = []
        self.patch_dim = patch_dim
        self._index = 0
        for file in os.listdir(img_dir):
            if file.split(".")[-2] + ".json" in os.listdir(json_dir):
                img_path = os.path.join(img_dir, file)
                json_path = os.path.join(json_dir, file.split(".")[-2] + ".json")
                with open(json_path, 'r') as json_file:
                    data = json.load(json_file)
                    img_size = (data.imageWidth, data.imageHeight)
                self.pages.append({
                    "img_path": img_path,
                    "json_path": json_path,
                    "img_size": img_size
                })
       
    def __getitem__(self, index):
        def num_patches(patch_size: (int, int), img_size: (int, int)):
            

        for i in self.pages:
            x = i.img_size[0] // self.patch_dim[2]
            y = i.img_size[1] // self.patch_dim[3]
            num_patches = x*y + x + y + 1
            if num_patches <= index:
                index -= num_patches
            else:
                if index == 0:
                    corner
                elif: 



    # def __next__(self):
    #     if self._index < len(self.data):
    #         result = self.data[self._index]
    #         self._index += 1
    #         return result
    #     else:
    #         raise StopIteration

            
def loadData(batch_size=2):
    batch_imgs=[]
    batch_data=[]
    for i in range(batch_size):
        idx = random.randint(0, len(imgs)-1)
        img = cv2.imread(os.path.join(imgs[idx], "Image.jpg"))
        img = cv2.resize(img, imageSize, cv2.INTER_LINEAR)
        maskDir = os.path.join(imgs[idx], "Vessels")
        masks = []
        for mskName in os.listdir(maskDir):
            vesMask = (cv2.imread(maskDir+'/'+mskName, 0) > 0).astype(np.uint8)  # Read vesse instance mask
            vesMask = cv2.resize(vesMask,imageSize,cv2.INTER_NEAREST)
            masks.append(vesMask)# get bounding box coordinates for each mask
        num_objs = len(masks)
        if num_objs==0: 
            return loadData() # if image have no objects just load another image
        boxes = torch.zeros([num_objs, 4], dtype=torch.float32)
        for i in range(num_objs):
            x, y, w, h = cv2.boundingRect(masks[i])
            boxes[i] = torch.tensor([x, y, x+w, y+h])
        masks = torch.as_tensor(masks, dtype=torch.uint8)
        img = torch.as_tensor(img, dtype=torch.float32)
        data = {}
        data["boxes"] = boxes
        data["labels"] =  torch.ones((num_objs,), dtype=torch.int64)   # there is only one class
        data["masks"] = masks
        batch_imgs.append(img)
        batch_data.append(data)  # load images and masks
    batch_imgs = torch.stack([torch.as_tensor(d) for d in batch_imgs], 0)
    batch_imgs = batch_imgs.swapaxes(1, 3).swapaxes(2, 3)
    return batch_imgs, batch_data


# train model
def train_model(model, num_epochs, optimizer, dataset):

    if not model.training:
         raise Exception("Model is not in train mode while training.")

    for i in range(num_epochs):
        images, targets = loadData()
        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k,v in t.items()} for t in targets]
        
        optimizer.zero_grad()
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        
        losses.backward()
        optimizer.step()
        
        print(i,'loss:', losses.item())
        if i%200==0:
                torch.save(model.state_dict(), str(i)+".torch")
                print("Save model to:",str(i)+".torch")

# test mode
def test_model(model, input):
    return model(input)


def maskrcnn_setup(num_classes):

    # load pretrained maskrcnn model from pytorch library
    model = maskrcnn_resnet50_fpn(weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT)

    # set number of classes in prediction
    in_features = model.roi_heads.box_predictor.cls_score.in_features 
    model.roi_heads.box_predictor=faster_rcnn.FastRCNNPredictor(in_features,num_classes=2)

    return model


if __name__ == "__main__":

    # get device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Available device: {device}")

    # load model with pretrained weights
    model = maskrcnn_setup(num_classes=2)
    print(model)
    model.to(device)

    # model.train()
    # train_model(model, num_epochs=5, optimizer=torch.optim.AdamW(params=model.parameters(), lr=1e-5), dataset)

    # # evaluation mode
    # model.eval()

    # # test model (will need to be made more complex in the future)
    # x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
    # predictions = test_model(model, x)