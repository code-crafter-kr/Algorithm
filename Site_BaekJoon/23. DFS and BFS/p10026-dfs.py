import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt", "r")

def dfs(x, y, z, board):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    elif board[x][y] != z:
        return False

    elif board[x][y] == z:
        board[x][y] = 1
        dfs(x + 1, y, z, board)
        dfs(x - 1, y, z, board)
        dfs(x, y + 1, z, board)
        dfs(x, y - 1, z, board)
        return True

# 입력값 받기
n = int(input())
board_A = []
board_B = []

for i in range (n):
    board_A.append([])
    board_B.append([])
    a = list(input())
    for x in a:
        board_A[i].append(x)
        if x == "R":
            board_B[i].append("G")
        else:
            board_B[i].append(x)
cnt_A = 0
cnt_B = 0
for i in ["R", "G", "B"]:
    for ii in range (n):
        for jj in range (n):
            if dfs(ii, jj, i, board_A) == True:
                cnt_A += 1

            if dfs(ii, jj, i, board_B) == True:
                cnt_B += 1

print(cnt_A, cnt_B)