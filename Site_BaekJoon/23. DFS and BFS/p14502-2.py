import sys
from collections import deque
from itertools import combinations
import copy
sys.stdin = open("input.txt")

x, y = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range (x)]
max_count = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

safe = []
Qx = deque()

cnt = 0

for i in range (x):
    for j in range (y):
        if board[i][j] == 2:
            Qx.append([i, j])
            cnt += 1
        
        elif board[i][j] == 1:
            cnt += 1
        
        elif board[i][j] == 0:
            safe.append([i, j])

for cases in combinations (safe, 3):
    cnt2 = 0
    Q = copy.deepcopy(Qx)
    board2 = copy.deepcopy(board)

    for (xx,yy) in cases:
        board2[xx][yy] = 1
    
    while Q:
        a, b = Q.popleft()

        for _ in range (4):
            new_a = a + dx[_]
            new_b = b + dy[_]

            if 0 <= new_a < x and  0 <= new_b < y:
                if board2[new_a][new_b] == 0:
                    board2[new_a][new_b] = 2
                    cnt2 += 1
                    Q.append([new_a, new_b])
    
    max_count = max(max_count, x*y - cnt - 3 - cnt2)

print(max_count)