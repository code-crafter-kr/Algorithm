import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

root = 1
n = int(input())

parent_node = [0] * (n+1) 
relation = [[] for _ in range (n+1)]

for i in range (n - 1):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [False] * (n+1)
def dfs(node = root):
    visited[node] = True

    for i in relation[node]:
        if visited[i]:
            continue
        if parent_node[i] == 0:
            parent_node[i] = node
        dfs(i)
    
parent_node[root] = 1
dfs()
for i in parent_node[2:]:
    print(i)