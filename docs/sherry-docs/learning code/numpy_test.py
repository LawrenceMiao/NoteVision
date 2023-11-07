import numpy as np

if __name__ == '__main__':
  test1 = np.ndarray([1, 2, 3])
  print(test1)

  test2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
  print(test2)
  print(test2[0])

  test3 = np.array([2, 5, 4])
  print(test3)
  print(np.sort(test3))

  test4 = np.array([3, 5, 5])

  print(np.concatenate((test3, test4)))
  print("ndim: " + str(test4.ndim))
  print("size: " + str(test4.size))
  print("shape: " + str(test4.shape))
  print("min: " + str(test4.min()))
  print("max: " + str(test4.max()))
  print("sum: " + str(test4.sum()))