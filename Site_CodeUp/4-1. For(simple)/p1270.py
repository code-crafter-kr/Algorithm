n = int(input())
list_A = [i for i in range(1, n+1)]
a = 0
for ii in list_A:
    if ii % 10 == 1:
        a += 1

print(a)