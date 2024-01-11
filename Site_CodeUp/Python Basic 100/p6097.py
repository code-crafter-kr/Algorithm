a, b = map(int,input().split())

board = [[0] * b for i in range (a)]

c = int(input())

for i in range (c):
    length, direction, y, x = map(int, input().split())
    y -= 1
    x -= 1

    if direction == 0:
        board[y][x] = 1
        for i in range (length-1):
            x = x + 1
            board[y][x] = 1

    else:
        board[y][x] = 1
        for i in range (length-1):
            y = y + 1
            board[y][x] =1
        
for ii in range (a):
    board[ii] = list(map(str, board[ii]))
    print(" ".join(board[ii]))