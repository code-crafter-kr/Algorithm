import sys
from collections import deque
sys.stdin = open( "input.txt", "r")

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, B, H = map(int, input().split())
list_A = []
Q = deque()

for i in range (H):
    list_A.append([list(map(int, input().split())) for _ in range (B)]) # 보드 생성

for xx in range (H):
    for yy in range (B):
        for zz in range (M):
            if list_A[xx][yy][zz] == 1:
                Q.append([xx, yy, zz, 0])

def bfs():
    global cnt
    while Q:
        x, y, z, cnt = Q.popleft()
        for i in range (6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= H or ny >= B or nz >= M:
                continue

            elif list_A[nx][ny][nz] != 0:
                continue

            elif list_A[nx][ny][nz] == 0:
                list_A[nx][ny][nz] = 1
                Q.append([nx, ny, nz, cnt + 1])
xxx = 0
bfs()
for ii in list_A:
    if xxx == 1:
        break
    for jj in ii:
        if jj.count(0) != 0:
            xxx = 1
            break

if xxx == 1:
    print(-1)
else:
    print(cnt)