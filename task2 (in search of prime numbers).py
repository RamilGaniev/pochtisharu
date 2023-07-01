import math
elem = 0
def primesearcher(elem):
    collector = []
    output = []
    collector.append(elem)
    for i in range(44):
        if elem % 2 == 0:
            elem += 21
        else:
            elem -= 1
        collector.append(elem)
    for elemi in collector:
        flag = 0
        for devider in range(2, int(math.sqrt(elem))+1):
            if elemi % devider == 0:
                flag = 1
        if flag == 0:
            output.append(elemi)
    return(output)
print(primesearcher(elem))

