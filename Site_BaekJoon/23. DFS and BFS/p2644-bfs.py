import sys
from collections import deque
sys.stdin = open("input.txt", "r")

Q = deque()
n = int(input()) 
a, b = map(int, input().split()) #7번 노드부터 확인
xx = int(input())

ans = [[] for _ in range (n + 1)]
graph = [[] for _ in range (n + 1)]
visited = [0] * (n + 1)

for i in range (xx):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, z):
    Q.append([a, z])
    while Q:
        n, cnt = Q.popleft()
        visited[n] = 1 #방문처리
        for i in graph[n]: #[2,3]
            if i == b:
                return cnt
            if visited[i] == 0:
                Q.append([i, cnt+1])
    return -1

print(bfs(a, 1))
