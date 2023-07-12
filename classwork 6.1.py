import csv
import matplotlib.pyplot as plt
import numpy as np
file = open('data2.csv', newline='')
x = []
y = []
fig, ax = plt.subplots()
try:
    reader = csv.reader(file)
    s = 0
    list = []
    for row in reader:
        s += 1
        list.append(row)
    for i in range(1, s):
        x.append(float(list[i][0]))
        y.append(float(list[i][1]))
finally:
    file.close()
x = np.array(x)
y = np.array(y)
print(list)
ax.plot(x, y)
plt.show()