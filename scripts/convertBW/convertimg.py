'''
input a PNG file
make the PNG black and white
save it as a new PNG
'''
import sys, errno

def bw_filter(input_img, output_img):
  try:
    with open(input_img, 'r') as file:
      print("s")
  except IOError as x:
    if x.errno == errno.ENOENT:
        print(input_img + ' does not exist.')
    elif x.errno == errno.EACCES:
        print(input_img + ' cannot be read.')
    else:
        print(input_img + ' has some unknown error.')
    exit()  

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("No input file given.")
    exit()
  else:
    input_img = sys.argv[1]

  if len(sys.argv) == 3:
    output_img = sys.argv[2]
    if ".png" not in output_img:
      output_img = output_img + ".png"
  else:
    output_img = input_img.replace(".img","") + "_bw.png"

  print(f"input file: {input_img}")
  print(f"output file: {output_img}")

  bw_filter(input_img, output_img)