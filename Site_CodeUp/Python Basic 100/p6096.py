board = [list(map(int, input().split())) for _ in range(19)]

A = int(input())
for i in range (A):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    for ii in range (19):
        board[y][ii] = 1 if board[y][ii] == 0 else 0

    for ii in range (19):
        board[ii][x] = 1 if board[ii][x] == 0 else 0

for ii in range (0,19):
    board[ii] = list(map(str, board[ii]))
    print(" ".join(board[ii]))