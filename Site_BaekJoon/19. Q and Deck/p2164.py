from collections import deque

lst = deque()
n = int(input())
for i in range(1, n+1):
    lst.append(i)

while len(lst) > 1:
    lst.popleft()
    a = lst.popleft()
    lst.append(a)

print(lst[0])