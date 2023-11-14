import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights, faster_rcnn


# load dataset
# train model

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

    # evaluation mode
    model.eval()

    # test model (will need to be made more complex in the future)
    x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
    predictions = test_model(model, x)