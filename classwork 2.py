import numpy

a = []
for i in range(8):
    tmp = []
    for j in range(8):
        if (i + j) % 2 == 0:
            tmp.append(0)
        else:
            tmp.append(1)
    a.append(tmp)
a = numpy.array(a, ndmin=2)
counter = 0
for h in range(8):
    for w in range(8):
        if a[h, w] == 1 and w < 6:
            counter += 1
print(counter)


