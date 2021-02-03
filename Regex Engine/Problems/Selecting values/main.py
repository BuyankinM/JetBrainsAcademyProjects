import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

aa = np.array([a, b, c, d])
print(aa[np.where(aa >= 45)])