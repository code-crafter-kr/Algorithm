import sys
sys. setrecursionlimit(10**7)

def dfs(n):
    visited[n] = 1
    for i in graph[n]: #[2,5]
        if visited[i] == 0:
            ans[i] = n
            dfs(i)


n = int(sys.stdin.readline())
visited = [0] * (n+1)
ans = [[] for _ in range (n+1)]
graph = [[] for _ in range (n+1)]

for _ in range (n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) 

dfs(1)
for i in range (2, n + 1):
    print(ans[i])