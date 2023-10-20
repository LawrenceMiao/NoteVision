'''
input a JSON file
remove image attribute of given JSON file
save it to an output JSON file
'''

import sys, json, errno

def remove_attribute(input_json, output_json):
  try:
    with open(input_json, 'r') as file:
      data = json.load(file)
      if "imageData" in data.keys():
        data.pop("imageData")
  except IOError as x:
    if x.errno == errno.ENOENT:
        print(input_json + ' does not exist.')
    elif x.errno == errno.EACCES:
        print(input_json + ' cannot be read.')
    else:
        print(input_json + ' has some unknown error.')
    exit()

  edited_data = json.dumps(data, indent=4)

  with open(output_json, 'w') as file:
    file.write(edited_data)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("No input file given.")
    exit()
  else:
    input_json = sys.argv[1]

  if len(sys.argv) == 3:
    output_json = sys.argv[2]
    if ".json" not in output_json:
      output_json = output_json + ".json"
  else:
    output_json = input_json.replace(".json","") + "_clean.json"
    
  print(f"input file: {input_json}")
  print(f"output file: {output_json}")

  remove_attribute(input_json, output_json)