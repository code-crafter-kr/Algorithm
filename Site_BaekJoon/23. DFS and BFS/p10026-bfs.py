import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z, board):
    Q = deque()
    Q.append([x, y])

    while Q:
        x , y = Q.popleft()
        
        for _ in range (4):
            nx = x + dx[_]
            ny = y + dy[_]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            elif board[nx][ny] != z:
                continue

            elif board[nx][ny] == z:
                board[nx][ny] = 0
                Q.append([nx, ny])

# 입력값 받기
n = int(input())
board_A = []
board_B = []

for i in range (n):
    board_A.append([])
    board_B.append([])
    a = list(input())
    for x in a:
        board_A[i].append(x) 
        if x == "R":
            board_B[i].append("G")
        else:
            board_B[i].append(x)
cnt_A = 0
cnt_B = 0


for i in ["R", "G", "B"]:
    for xx in range (n):
        for yy in range (n):
            if board_A[xx][yy] == i:
                board_A[xx][yy] = 0
                bfs(xx , yy, i, board_A)
                cnt_A += 1
            
            if board_B[xx][yy] == i:
                board_B[xx][yy] = 0
                bfs(xx, yy, i, board_B)
                cnt_B += 1
                
print(cnt_A, cnt_B)