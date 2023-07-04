import numpy as np
import matplotlib.pyplot as plt
import random
'''board = np.empty(64).reshape(8, 8)
cells = np.nditer(board, flags=['multi_index'])
counter = 0
for cell in cells:
    if (cells.multi_index[0] + cells.multi_index[1]) % 2 == 0 and cells.multi_index[1] <= 5:
        counter += 1
print(counter)'''
"""n = int(input())
arr = np.empty((2, n), dtype='i')
for i in range(n):
    arr[0, i] = 2 ** (i + 1)
    arr[1, i] = (i + 1) ** 2
final = np.empty(0)
for i in range(n):
    znach = i ** 2
    while znach % 2 == 0 or znach % 5 == 0:
        if znach % 2 == 0:
            znach = znach // 2
        elif znach % 5 == 0:
            znach = znach // 5
    if i == 1:
        final.append(2 ** i)"""
'''data = [1, 2, 3, 4, 4]
x = np.arange(0, np.size(data))
fig, ax = plt.subplots()
ax.plot(x, data)
#ax.bar(x, data)
#ax.scatter(x, data)
plt.show()'''
data = [0] * 100
for j in range(100000):
    s = 0
    for i in range(100):
        s += random.randint(0, 1)
    data[s-1] += 1
for j in range(100):
    data[j] = data[j] / 100000

x = np.arange(0, np.size(data))
fig, ax = plt.subplots()
ax.bar(x, data)
plt.show()
