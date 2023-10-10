'''
input a json file
edit the given json file and save it 
'''

import sys, json

def remove_attribute(input_json):
  with open(input_json) as file:
    data = json.load(file)
    if "imageData" in data.keys():
      data.pop("imageData")

if __name__ == "__main__":
  input_json = sys.argv[1]

  print(f"input file: {input_json}")

  remove_attribute(input_json)