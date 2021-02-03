import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)

row1, row2 = int(input()), int(input())

print(array[row1].astype(np.str_))
print(array[row2].astype(np.float64))