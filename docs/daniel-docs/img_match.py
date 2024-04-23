import cv2

def imgMatch(template_path, image_path):
    # Read template and target image
    template = cv2.imread(template_path)
    target = cv2.imread(image_path)

    # Convert images to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(target_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    match_loc = max_loc

    # Draw a rectangle around the matched region
    height, width = template_gray.shape
    top_left = match_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(target, top_left, bottom_right, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Matched Image', target)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    p1 = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/docs/daniel-docs/kfp1.jpg"
    p2 = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/docs/daniel-docs/kfp2.jpg"
    imgMatch(p2, p1)