import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(n, z):
    Q = deque()
    Q.append([n, z])
    visited = [0 for _ in range (xx+1)]
    visited[n] = 1
    sum = 0

    while Q:
        x, y = Q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                sum += y
                visited[i] = 1
                Q.append([i, y+1])
    return sum

xx, yy = map(int, input().split())
graph = [[] for _ in range (xx+1)]

for i in range (yy):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

lst = []
for i in range (xx):
    A = bfs(i+1, 1)
    lst.append([A, i+1])
lst.sort()
print(lst[0][1])