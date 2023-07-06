import string

a = string.ascii_lowercase
A = string.ascii_uppercase

str0 = input()
k = input()


def Cezar(str0, k):
    exstr = []
    str0 = list(str0)
    for i in str0:
        if i in a:
            let = chr((ord(i) - ord('a') + int(k)) % 26 + ord('a'))
            exstr.append(let)
        elif i in A:
            let = chr((ord(i) - ord('A') + int(k)) % 26 + ord('A'))
            exstr.append(let)
        else:
            exstr.append(i)
    return ''.join(exstr)


print(Cezar(str0, k))
