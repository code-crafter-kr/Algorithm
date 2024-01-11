board = [[0]*19 for _ in range(19)]

A = int(input())
for i in range (A):
    x,y = map(int, input().split()) 
    board[x-1][y-1] = 1

for ii in range (0,19):
    board[ii] = list(map(str, board[ii]))
    print(" ".join(board[ii]))