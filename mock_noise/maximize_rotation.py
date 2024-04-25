"""
We need a way to normalize the orientation of sheet music such that the barlines 
and ledger lines are vertically and horizontally aligned. To do this, we simply 
choose a roated orientation of the image such that the count of edges from the 
horizontal and vertical sobel operators is maximized. 
"""

import cv2
import numpy as np
import music_noise

img = cv2.imread("noise_sample1.png", cv2.IMREAD_GRAYSCALE)


max_edge_pixels = -1
best_angle = 0

# iterate through angles that come from slight changes in scanned papers
for angle in range(-30, 30):
    rotated_img = music_noise.rotate(img, angle)

    # get sobel kernals
    sobel_horizontal = cv2.Sobel(rotated_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_vertical = cv2.Sobel(rotated_img, cv2.CV_64F, 0, 1, ksize=3)

    # calculate total edge detection from vetical and horizontal operators.
    num_horizontal_edges = np.sum(sobel_horizontal == 0)
    num_vertical_edges = np.sum(sobel_vertical == 0)

    total_edge_pixels = num_horizontal_edges + num_vertical_edges

    # get optimal angle
    if total_edge_pixels > max_edge_pixels:
        max_edge_pixels = total_edge_pixels
        best_angle = angle

rotated_img = music_noise.rotate(img, best_angle)

cv2.imshow("asdfasdf", img)
cv2.imshow("asdgasfd", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
