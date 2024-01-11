import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**7)

n = int(input()) # 
a, b = map(int, input().split()) #7번 노드부터 확인
xx = int(input())

ans = [[] for _ in range (n + 1)]
graph = [[] for _ in range (n + 1)]
visited = [0] * (n + 1)

for i in range (xx):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

xxx = 0
def dfs(n, x, z):
    visited[n] = 1
    global xxx
    for i in graph[n]: #[2,3]
        if i == x:
            xxx = 1
            return print(z+1)
        if visited[i] == 0:
            ans[i] = n
            dfs(i, x, z + 1)

dfs(a, b, 0) #a번 노드부터 확인

if xxx == 0:
    print(-1)