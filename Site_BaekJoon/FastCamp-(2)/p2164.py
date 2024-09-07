from collections import deque

t = int(input())
n = deque()

if t == 1:
    print(1, end = "")
else:
    for i in range (t):
        n.append(i+1)
    while t != 1:
        n.popleft()
        n.append(n.popleft())
        t -= 1

    print(n[0], end = "")
