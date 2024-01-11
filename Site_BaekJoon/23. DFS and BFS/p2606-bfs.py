import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(n):
    Q = deque()
    Q.append(graph[n])

    while Q:
        nords = Q.popleft() #[2, 5]
        for i in nords:
            if visited[i] == 0:
                Q.append(graph[i])
                visited[i] = 1


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range (N+1)]
visited = [0] * (N+1)

for _ in range (M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) 


bfs(1)
print(visited.count(1)-1)