import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)

def dfs(x, y):
    global cnt
    visited[x][y] = 1

    if x == M - 1 and y == N - 1:
        cnt += 1
    
    else:
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] < board[x][y] and visited[nx][ny] == 0:
                dfs(nx, ny)
                visited[nx][ny] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())

cnt = 0
board = [list(map(int, sys.stdin.readline().split())) for _ in range (M)]
visited2 = [0 for _ in range (N)]
visited = [visited2.copy() for _ in range (M)]


dfs(0, 0)
print(cnt)