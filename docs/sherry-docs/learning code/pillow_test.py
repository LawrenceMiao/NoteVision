from PIL import Image

if __name__ == '__main__':
  img = Image.open("00000000.jpg")
  # img.show()

  print("size: " + str(img.size))
  print("format: " + str(img.format))
  print("mode: " + str(img.mode))

  # img.show()
  img = img.rotate(45, Image.NEAREST, expand = 1)
  # img.show()

  # img.show()
  img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
  # img.show()

  # img.show()
  img = img.resize((200, 200))
  # img.show()