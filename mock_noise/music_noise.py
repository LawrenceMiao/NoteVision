import cv2
import random


def resize(img, scale):
    new_width = img.shape[0] * scale
    new_height = img.shape[1] * scale

    return cv2.resize(image, (new_width, new_height))


def rotate(img, angle):
    angle = 20

    height, width = img.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    return cv2.warpAffine(image, rotation_matrix, (width, height))


image = cv2.imread("sample1.png", cv2.IMREAD_GRAYSCALE)
# image = resize(image, 2)

_, binary_image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

superimposed_image = cv2.bitwise_or(binary_image, image)


edges = cv2.Canny(binary_image, 100, 200)
# cv2.imshow("Binary Image", binary_image)
cv2.imshow("Detected Edges", superimposed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
