import numpy as np

a = int(input())
b = int(input())
c = int(input())

aa = np.array([a, b, c])
print(np.all(aa > 15))