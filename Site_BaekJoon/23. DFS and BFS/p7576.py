import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

a, b = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range (b)]

Q = deque()
for i in range (b):
    for j in range(a):
        if board[i][j] == 1:
            Q.append([i, j, 1])

while Q:
    x, y, z = Q.popleft()

    for i in range (4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if new_y < 0 or new_x < 0 or new_y >= a or new_x >= b:
            continue

        elif board[new_x][new_y] == -1:
            continue

        elif board[new_x][new_y] == 0:
            Q.append([new_x, new_y, z+1])
            board[new_x][new_y] = z 


for i in board:
    
    if i.count(0) >= 1:
        z = 0
        break
print(z-1)
