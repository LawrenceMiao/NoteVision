def openFile(filename, mode):
  return open(filename, mode)

def closeFile(file):
  file.close()

def readLineByLine(file):
  for line in file:
    print(line)

if __name__ == '__main__':
  test_file1 = openFile("one_quote1.txt", "rt")
  # print(test_file1.read())
  readLineByLine(test_file1)
  closeFile(test_file1)

  test_file2 = openFile("one_quote2.txt", "a")
  test_file2.write("\n comment: interesting quote")
  closeFile(test_file2)

  test_file2 = openFile("one_quote2.txt", "r")
  readLineByLine(test_file2)
  closeFile(test_file2)

  test_file3 = openFile("test_image.png", "rb")
  # print(test_file3.read())
  closeFile(test_file3)

  test_file4 = openFile("test.txt", "x")
  closeFile(test_file4)

  test_file5 = openFile("created_quote.txt", "w")
  test_file5.write("some inspirational stuff - inspirational person")
  closeFile(test_file5)

  test_file6 = openFile("two_quotes.txt", "r")
  # print(test_file6.readline())
  readLineByLine(test_file6)
  closeFile(test_file6)
