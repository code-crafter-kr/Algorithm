a, b = map(int, input().split())
list_A = [[] for _ in range (a)]
c = 1
z = 0

if a % 2 == 0:
    x = 1
else:
    x = 0

for jj in range (b):
    if jj % 2 == 0:
        for ii in range (a-1, -1, -1):
            list_A[ii].append(c)
            c += 1
    else:
        for ii in range(a):
            list_A[ii].append(c)
            c += 1

for i in range (a-1 ,-1 ,-1):
    list_A[i].reverse()
    print(*list_A[i])