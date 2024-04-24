import cv2

def resizeImage(img, maxWidth, maxHeight):
    # Get original image dimensions
    height, width = img.shape[:2]

    # Calculate aspect ratio
    aspectRatio = width / height

    # Resize based on the larger dimension
    if width > height:
        newWidth = min(width, maxWidth)
        newHeight = int(newWidth / aspectRatio)
    else:
        newHeight = min(height, maxHeight)
        newWidth = int(newHeight * aspectRatio)

    # Perform resizing
    resizedImg = cv2.resize(img, (newWidth, newHeight), interpolation=cv2.INTER_AREA)

    return resizedImg

def imgMatch(templatePath, imagePath, maxDisplayWidth = 800, maxDisplayHeight = 600):
    # Read template and target image
    template = cv2.imread(templatePath)
    target = cv2.imread(imagePath)

    # Resize images if they are larger than maximum display size
    if max(template.shape[0], template.shape[1], target.shape[0], target.shape[1]) > maxDisplayWidth or max(template.shape[0], template.shape[1], target.shape[0], target.shape[1]) > maxDisplayHeight:
        template = resizeImage(template, maxDisplayWidth, maxDisplayHeight)
        target = resizeImage(target, maxDisplayWidth, maxDisplayHeight)

    # Convert images to grayscale
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(targetGray, templateGray, cv2.TM_CCOEFF_NORMED)

    # Get the location of the best match (minVal, maxVal, and minLoc are filler vars)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    matchLoc = maxLoc

    # Draw a rectangle around the matched region
    height, width = templateGray.shape
    topLeft = matchLoc
    bottomRight = (topLeft[0] + width, topLeft[1] + height)
    cv2.rectangle(target, topLeft, bottomRight, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Matched Image', target)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    p1 = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/docs/daniel-docs/kfp1.jpg"
    p2 = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/docs/daniel-docs/kfp2.jpg"
    imgMatch(p2, p1)