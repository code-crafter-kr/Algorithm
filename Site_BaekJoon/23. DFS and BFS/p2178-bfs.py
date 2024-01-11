import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(x,y,z):
    Q = deque()
    Q.append([x,y,z])

    while Q:
        x, y, z= Q.popleft()

        for d in range (4):
            new_y = y + dy[d]
            new_x = x + dx[d]

            if new_y < 0 or new_x < 0 or new_y >= b or new_x >= a:
                continue

            elif board[new_x][new_y] == "1":
                board[new_x][new_y] = z + 1
                Q.append([new_x, new_y, z + 1])
                continue

            elif board[new_x][new_y] == "0":
                continue

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

a, b = map(int, sys.stdin.readline().split())

board = [list(input()) for _ in range (a)]

bfs(0, 0, 1)
print(board[-1][-1])

for i in board:
    print(i)