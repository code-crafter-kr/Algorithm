import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()

        for _ in range (4):
            nx = x + dx[_]
            ny = y + dy[_]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            elif visited[nx][ny] <= i:
                continue

            else:
                visited[nx][ny] = 0
                Q.append([nx, ny])

n = int(input())

temp = []
visited2 = [list(map(int, input().split())) for _ in range (n)]

for i in range (0, 101):
    visited = []
    for j in visited2:
        visited.append(j.copy())
    cnt = 0

    for ii in range (n):
        for jj in range (n):
            if visited[ii][jj] > i:
                visited[ii][jj] = 0
                bfs(ii, jj)
                cnt += 1
    temp.append(cnt)

print(max(temp))