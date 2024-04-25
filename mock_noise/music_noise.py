import cv2
import random


# utility to resize image
def resize(img, scale):
    new_width = img.shape[0] * scale
    new_height = img.shape[1] * scale

    return cv2.resize(image, (new_width, new_height))


# utility to add sheet music noise to binary image
def dot_noise(binary_img, num_pixels):
    for _ in range(num_pixels):
        x = random.randint(0, binary_img.shape[1] - 1)
        y = random.randint(0, binary_img.shape[0] - 1)

        if binary_img[y, x] == 255:
            binary_img[y, x] = 0
    return binary_img


# utility to invert binary image
def invert(binary_img):
    return cv2.bitwise_not(binary_img)


# utility to rotate image with specified degree
def rotate(img, angle):
    angle = 20

    height, width = img.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    return cv2.warpAffine(image, rotation_matrix, (width, height))


file = "sample3.png"

if __name__ == "__main__":

    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    _, binary_image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)

    edges = cv2.Canny(binary_image, 100, 200)

    edges = dot_noise(edges, 2000000)

    superimposed_image = cv2.bitwise_or(binary_image, edges)
    superimposed_image = invert(superimposed_image)

    cv2.imwrite(f"noise_{file}", superimposed_image)
