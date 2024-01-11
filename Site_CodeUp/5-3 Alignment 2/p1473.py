a, b = map(int, input().split())
list_A = [[] for _ in range (a)]
c = 1

if a % 2 == 1:
    x = 1
else:
    x = 0

for ii in range (a-1, -1, -1):
    for jj in range (b):
        list_A[ii].append(c)
        c += 1

for i in range (a):
    if i % 2 == x:
        list_A[i].reverse()
        print(*list_A[i])
    else:
        print(*list_A[i])
