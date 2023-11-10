'''
input: PNG or JPEG file
output: black and white threshold PNG image
'''
import sys, cv2

def bw_filter(input_img):
  grey_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
  bw_img = cv2.threshold(grey_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  return bw_img[1]

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("No input file given.")
    exit()

  input_img = sys.argv[1]
    
  file_type = "." + input_img.rsplit('.', 1)[1]

  if len(sys.argv) == 3:
    output_img = sys.argv[2]
    if ".png" not in output_img:
      output_img = output_img + ".png"
  else:
    output_img = input_img.replace(file_type,"") + "_bw.png"

  bw_img = bw_filter(cv2.imread(input_img))
  cv2.imwrite(output_img, bw_img)

  print(f"Applied black and white thresholding to {input_img}.")
  print(f"Input file: {input_img}")
  print(f"Output file: {output_img}")