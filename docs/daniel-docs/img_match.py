import cv2

def image_match(template_path, target_path):
    # Load template and target images
    template = cv2.imread(template_path, 0)
    target = cv2.imread(target_path, 0)

    # Resize template image to match the size of the target image
    template = cv2.resize(template, (target.shape[1], target.shape[0]))

    # Perform template matching
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    height, width = template.shape

    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(target, top_left, bottom_right, 255, 2)

    # Display the result
    cv2.imshow('Image Match', target)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_match('kfp1.jpg', 'kfp2.jpg')