import numpy as np


num_list = []
for _ in range(6):
    num_list.append(int(input()))


a = np.array([num_list[:2], num_list[2:4]])
b = np.array(num_list[4:])

print(a @ b)