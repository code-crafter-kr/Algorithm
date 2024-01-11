import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(x, y, stack):
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()

        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            elif board[nx][ny] == 1:
                continue

            elif board[nx][ny] == 0:
                board[nx][ny] = 1
                stack += 1
                Q.append([nx, ny])
    return stack

#board 전처리
N, M, K = map(int, sys.stdin.readline().split())
board_p = [0] * (M)
board = [board_p.copy() for _ in range (N)]

for _ in range (K):
    a, b, c, d = map(int, sys.stdin.readline().split()) # 0 2 4 4 >> 2 - > 4 / 0 > 4
    for ii in range (b, d):
        for jj in range (a, c):
            board[ii][jj] = 1 #막힌곳 표시

# bfs 실행
a = 0
cnt_lst = []
for xx in range (N):
    for yy in range (M):
        cnt = 0
        if board[xx][yy] == 0:
            board[xx][yy] = 1
            z = bfs(xx, yy, 1)
            cnt_lst.append(z) #영역의 넓이 저장
            a += 1 #영역의 개수 저장
            
#출력
cnt_lst.sort() #오름차순을 위한 sort()
print(a)
print(* cnt_lst)