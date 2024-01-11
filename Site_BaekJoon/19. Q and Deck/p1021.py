from collections import deque

N, M = map(int, input().split())
list_A = list(map(int, input().split()))

x = 0
lst = deque()

for i in range(1, N+1):
    lst.append(i)

for i in list_A:
    while True:
        if lst.index(i) != 0:
            if lst.index(i) > len(lst) - lst.index(i):
                lst.rotate(1)
                x += 1
            else:
                lst.rotate(-1)
                x += 1
        else:
            lst.popleft()
            break
print(x)

