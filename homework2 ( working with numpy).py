import numpy

n = int(input())
list = [[], []]
output = []
for i in range(n):
    list[0].append(2 ** i)
    list[1].append(i ** 2)
print(numpy.array(list, ndmin=2))
for j in range(1, n + 1):
    znach = j ** 2
    while znach % 2 == 0 or znach % 5 == 0:
        if znach % 2 == 0:
            znach = znach // 2
        elif znach % 5 == 0:
            znach = znach // 5
    if znach == 1:
        output.append(2 ** j)

print(numpy.array(output))
