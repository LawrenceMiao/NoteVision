import cv2
import numpy as np
import music_noise

img = cv2.imread("noise_sample1.png", cv2.IMREAD_GRAYSCALE)


max_edge_pixels = -1
best_angle = 0

for angle in range(-30, 30):
    rotated_img = music_noise.rotate(img, angle)

    sobel_horizontal = cv2.Sobel(rotated_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_vertical = cv2.Sobel(rotated_img, cv2.CV_64F, 0, 1, ksize=3)

    num_horizontal_edges = np.sum(sobel_horizontal == 0)
    num_vertical_edges = np.sum(sobel_vertical == 0)

    total_edge_pixels = num_horizontal_edges + num_vertical_edges

    if total_edge_pixels > max_edge_pixels:
        max_edge_pixels = total_edge_pixels
        best_angle = angle

rotated_img = music_noise.rotate(img, best_angle)

cv2.imshow("asdfasdf", img)
cv2.imshow("asdgasfd", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
