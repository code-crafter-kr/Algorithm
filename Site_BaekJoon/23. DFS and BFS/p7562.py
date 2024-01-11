import sys
sys.stdin = open("input.txt", "r")
from collections import deque
test_case = int(input())

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [-2, 2, -2, 2, 1, -1, 1, -1]

def bfs():
    while Q:
        x, y, z = Q.popleft()

        if x == xx and y == yy:
            return z

        for i in range (8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                pass

            elif chess[nx][ny] == 1:
                pass

            elif chess[nx][ny] == 0:
                chess[nx][ny] = 1
                Q.append([nx, ny, z+1])
        

for i in range (test_case):
    I = int(input())
    chess = []
    board = [0 for _ in range (I)]
    for _ in range (I):
        chess.append(board.copy())
    
    Q = deque()
    a, b = map(int, input().split()) # 초기 위치
    chess[a][b] = 1
    Q.append([a, b, 0])
    xx, yy = map(int, input().split()) # 도달 위치
    
    print(bfs())



