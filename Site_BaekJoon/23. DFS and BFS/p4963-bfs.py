import sys
from collections import deque
sys.stdin = open("input.txt", "r")
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]
def bfs(x, y):
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()
        for _ in range (8):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or ny < 0 or nx >= b or ny >= a:
                pass

            elif visited[nx][ny] == 0:
                pass

            elif visited[nx][ny] == 1:
                visited[nx][ny] = 0
                Q.append([nx, ny])


while True:
    a, b = map(int, input().split())
    cnt = 0

    if a == 0 and b == 0:
        break

    if a > 1:
        visited = [list(map(int, input().split())) for _ in range (b)] # 두 줄

    else:
        visited = [int(input()) for _ in range (b)] # 맵 생성 

    if visited == [0]: # xy가 1 1 일때
        print(cnt)

    elif visited == [1]:
        print(1)

    elif a > 1 and b > 1:
        for xx in range (b):
            for yy in range (a):
                if visited[xx][yy] == 1:
                    bfs(xx,yy)
                    cnt += 1

        print(cnt)


    
