import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])

    while Q:
        a, b = Q.popleft()

        for _ in range (4):
            na = a + dy[_]
            nb = b + dx[_]

            if na < 0 or nb < 0 or na >= width or nb >= length:
                continue

            elif board[na][nb] == 1:
                board[na][nb] = 0
                Q.append([na, nb])
            

n = int(input())

for i in range (n):
    temp = []
    length, width, z = map(int, input().split()) #세로가 8 가로가 1
    board = [[0] * length for _ in range (width)]
    cnt = 0

    for j in range (z):
        q, p = map(int, input().split())
        board[p][q] = 1
    

    for xx in range (width):
        for yy in range (length):
            if board[xx][yy] == 1:
                bfs(xx, yy)
                cnt += 1
    
    print(cnt)