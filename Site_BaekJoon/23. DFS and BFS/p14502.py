import sys
from collections import deque

sys.stdin = open("input.txt", "r")

x, y = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range (x)]
max_count = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(): #바이러스가 퍼지게하는 dfs와 바이러스 개수를 세어준다.
    global board
    board2 = []
    for i in board:
        board2.append(i.copy())

    Q = deque()
    cnt = 0
    for i in range (x): #바이러스가 있는곳 전부 추출
        for j in range(y):
            if board[i][j] == 2:
                Q.append([i, j])
                cnt += 1
            
            if board[i][j] == 1:
                cnt += 1
            
    while Q:
        a, b = Q.popleft()

        for i in range (4):
            new_a = a + dx[i]
            new_b = b + dy[i]

            if 0 <= new_a < x and  0 <= new_b < y:
                if board[new_a][new_b] == 0:
                    board[new_a][new_b] = 2
                    cnt += 1
                    Q.append([new_a, new_b])
    
    board = []
    for i in board2:
        board.append(i.copy())
    return (x*y - cnt) #바이러스가 다 퍼진 뒤 안전구역의 개수


def make_wall(z):
    global max_count
    if z == 3:
        max_count = max(max_count, bfs()) 
        return
    
    else:
        for xx in range (x):
            for yy in range (y):
                if board[xx][yy] == 0:
                    board[xx][yy] = 1
                    make_wall(z+1)
                    board[xx][yy] = 0

make_wall(0)
print(max_count)


# while True:
#     board = []

#     for i in board_original:
#         board.append(i.copy())

#     bfs()
#     a = 0
#     for i in board:
#         x = i.count(0)
#         a += x
        
#     print(a)

#벽을 세우고 제거하기를 반복시켜야한다.