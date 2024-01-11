import sys
sys.stdin = open("input.txt", "r")
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_num = 1000000

def bfs(board):
    Q = deque()
    Q.append([0, 0, 1, 0])

    while Q:
        x, y, z, d = Q.popleft()

        if x == xx-1 and y == yy-1:
            return z

        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= xx or ny >= yy:
                pass

            else:
                if board[nx][ny] == 1 and d == 0: # 벽 뚫기 이번만 넘어갑니다.
                    Q.append([nx, ny, z + 1, 1]) # 벽을 뚫었음을 의미 ' 1 '

                elif board[nx][ny] == 0 and d == 1: # 벽을 건너뛰었으면 그냥 가던길 가기
                    board[nx][ny] = 2 #벽을 뚫지 않고 길을 지나간 길
                    Q.append([nx, ny, z + 1, 1])
                
                elif (board[nx][ny] == 0 or board[nx][ny] == 2) and d == 0:
                    board[nx][ny] = 1
                    Q.append([nx, ny, z + 1 ,0]) #벽 안뚫기
                
                elif board[nx][ny] == 1 and d == 1: #더이상 진행 x
                    pass

    return -1

# def make_wall():
#     global min_num
#     for i in range (xx):
#         for j in range (yy):
#             if board2[i][j] == 1:
#                 board = copy.deepcopy(board2)
#                 board[i][j] = 0
#                 a = bfs(board)

#                 if a == xx + yy - 1:
#                     min_num = 0
#                     return print(a)

#                 if a > 0 and min_num > a:
#                     min_num = min(a, min_num)


xx, yy = map(int, sys.stdin.readline().split())
board2 = []
for i in range (xx):
    a = list(map(int, list(sys.stdin.readline().rstrip())))
    board2.append(a)

print(bfs(board2))