import cv2
import random


def rotate(img, angle):
    angle = 20

    height, width = img.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    return cv2.warpAffine(image, rotation_matrix, (width, height))


image = cv2.imread("sample1.png", cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
