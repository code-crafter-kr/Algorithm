import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 9) 

def dfs(x, y, cnt):
    if x == a-1 and y == b-1: #끝점까지의 모든경로의 이동횟수중 최단경로
        global Min
        if cnt < Min:
            Min = cnt
            return

    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or a <= nx or ny < 0 or b <= ny:
            pass

        elif board[nx][ny] == "1" and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

a, b = map(int, sys.stdin.readline().split())
board = [list(input()) for _ in range (a)]
visited = [[0] * b for _ in range (a)]
Min = a * b
dfs(0, 0, 1)
print(Min)