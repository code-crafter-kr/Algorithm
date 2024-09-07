import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
relation = {}
for i in range(n):
    relation[i+1] = []
m = int(input())
for i in range (m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

cnt = 0
def dfs(node, visited):
    global cnt
    if node in visited:
        return
    else:
        visited[node] = True
        cnt += 1
        for i in relation[node]:
            dfs(i, visited)

dfs(1, {})
print(cnt-1, end = "")