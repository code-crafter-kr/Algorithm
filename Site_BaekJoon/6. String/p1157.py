# 문자열 문제 '알파벳 찾기'
L = input(str())
L = L.lower()

F = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

list_N = []
for i in F:
    A = L.count(i)
    list_N.append(A)

list_A = list_N[:]
list_A.sort()

if list_A[25]  == list_A[24]:
    print("?")

else:
    end_N =int(list_N.index(list_A[25]))
    print(F[end_N].upper())

