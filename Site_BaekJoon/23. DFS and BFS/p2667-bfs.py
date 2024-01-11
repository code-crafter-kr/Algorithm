import sys
sys.stdin = open("input.txt", "r")
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range (n)]
temp = []

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    global z
    z = 0
    while Q:
        a, b = Q.popleft()
        for i in range (4):
            na = a + dx[i]
            nb = b + dy[i]

            if na < 0 or nb < 0 or n <= na or n <= nb:
                pass

            elif board[na][nb] == '0':
                pass

            else:
                board[na][nb] = '0'
                z = z + 1
                Q.append([na, nb])
    return z


for i in range (n):
    for j in range (n):
        if board[i][j] == '1':
            d = bfs(i, j)
            if d == 0:
                d += 1
            temp.append(d)

print(len(temp))
temp.sort()
for x in temp:
    print(x)