# import stuff
import torch
from torchvision.models import detection


# define model
# load new model

model = detection.maskrcnn_resnet50_fpn(weights=detection.MaskRCNN_ResNet50_FPN_Weights.DEFAULT)
model.eval()
print(model)
x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
predictions = model(x)
print(predictions)
# load dataset
# train model
# test model
