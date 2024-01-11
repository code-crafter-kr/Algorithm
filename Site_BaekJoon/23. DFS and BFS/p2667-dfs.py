import sys
sys.stdin = open("input.txt", "r")
# 0 1 1 0 1 0 0 # [0,0] - [0,6]
# 0 1 1 0 1 0 1
# 1 1 1 0 1 0 1
# 0 0 0 0 1 1 1
# 0 1 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 1 1 1 0 0 0 # [6,0] - [6,6]

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range (n)]
temp = []

def dfs(x, y):
    global d
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    elif board[x][y] == '0':
        return False

    elif board[x][y] == '1':
        board[x][y] = '0'
        d = d + 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
z = 0

for i in range (n):
    for j in range (n):
        d = 0
        dfs(i, j)
        if d > 0:
            temp.append(d)
            z += 1

print(z)
temp.sort()
for i in temp:
    print(i)