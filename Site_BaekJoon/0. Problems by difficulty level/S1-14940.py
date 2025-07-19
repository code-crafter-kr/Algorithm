import sys
from collections import deque

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

# 초기 2 시작점
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            start_i, start_j = i, j

# 초기 값
answer = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
que = deque()
que.append((start_i, start_j))
answer[start_i][start_j] = 0

def bfs():
    while que:
        i, j = que.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and lst[ni][nj] == 1:
                    visited[ni][nj] = True
                    answer[ni][nj] = answer[i][j] + 1
                    que.append((ni, nj))

bfs()

# 갈 수 없는 땅은 0으로 초기화
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            answer[i][j] = 0

# 출력
for row in answer:
    print(*row)