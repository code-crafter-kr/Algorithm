import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(n):
    Q = deque()
    for i in graph[n]:
        Q.append(i)

    while Q:
        a = Q.popleft()

        if visited[a] == 0:
            visited[a] = 1
            for i in graph[a]:
                Q.append(i)

        else:
            pass
        

N, M = map(int, sys.stdin.readline().split()) # 노드의 개수 / 간선의 개수
graph = [[] for _ in range (N+1)]

visited = [0] * (N+1)
cnt = 0

for _ in range (M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) 

for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)