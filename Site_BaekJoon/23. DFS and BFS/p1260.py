import sys
sys.setrecursionlimit(10**7)
from collections import deque
sys.stdin = open("input.txt", "r")

def dfs(n):
    print(n, end = " ")
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)

def bfs(n):
    Q = deque()
    print(n, end = " ")
    visited[n] = 1
    Q.append(graph[n]) #첫번째
    while Q:
        nords = Q.popleft()
        for i in nords:
            if visited[i] == 0:
                print(i, end = " ")
                Q.append(graph[i])
                visited[i] = 1

a, b, c = map(int, sys.stdin.readline().split())

visited = [0] * (a + 1)

graph = [[] for _ in range (a+1)]

for _ in range (b):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u) 

for i in graph:
    i.sort()

dfs(c)
visited = [0] * (a + 1)
print("")
bfs(c)
