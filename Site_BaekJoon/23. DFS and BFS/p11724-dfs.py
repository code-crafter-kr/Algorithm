import sys
sys.setrecursionlimit(10**7)

def dfs(n):
    visited[n] = 1
    for i in graph[n]: #[2,5]
        if visited[i] == 0:
            dfs(i)

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
        dfs(i)
        cnt += 1

print(cnt)