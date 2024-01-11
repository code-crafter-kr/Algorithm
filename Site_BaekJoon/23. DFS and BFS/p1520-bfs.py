import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs():
    global cnt

    while Q:
        x, y = Q.popleft()

        if x == M - 1 and y == N - 1:
            cnt += 1
        
        else:
            for i in range (4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N and board[nx][ny] < board[x][y]:
                    Q.append([nx, ny])
                    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())
Q = deque()
cnt = 0
board = [list(map(int, sys.stdin.readline().split())) for _ in range (M)]

Q.append([0, 0])
bfs()
print(cnt)