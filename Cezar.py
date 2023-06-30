import string
a = string.ascii_lowercase
A = string.ascii_uppercase

str0 = input()
k = input()
def move(j, k):
    return (j + int(k)) % 26
def Cezar(str0, k):
    exstr = []
    str0 = list(str0)
    for letter in str0:
        if letter in a:
            for j in range(26):
                if a[j] == letter:
                    exstr.append(a[move(j, k)])
        if letter in A:
            for j in range(26):
                if A[j] == letter:
                    exstr.append(A[move(j, k)])
    return "".join(exstr)

def reversedCezar(str0, k):
    return(Cezar(str0, -k))

print(Cezar(str0, k))
