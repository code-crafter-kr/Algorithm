import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")

def dfs(n):
    visited[n] = 1
    for i in graph[n]: #[2,5]
        if visited[i] == 0:
            dfs(i)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range (N+1)]
visited = [0] * (N+1)
for _ in range (M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) 


dfs(1)

print(visited.count(1)-1)