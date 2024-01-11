M = int(input())
N = int(input())
b = 0
list_A = []

T = [i for i in range (M, N+1)]

for i in range (len(T)):
    a = int(T[i])

    if a == 1:
        pass
    elif a == 2:
        b = 2
        list_A.append(b)

    elif a != 1 and a != 2:
        for ii in range (2, a):
            if a % ii == 0:
                break
            elif a % ii != 0 and ii == a-1:
                b = b + a
                list_A.append(b)

if b == 0:
    print(-1)
else:
    print(b)
    print(list_A[0])