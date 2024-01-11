import sys
sys.stdin = open("input.txt", "r")

def dfs(x, y, ans): 

    global count
    count = max(count, ans)
    if count == 26:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < a and 0 <= ny < b and visited[ord(board[nx][ny])-65] == 0:
            visited[ord(board[nx][ny])-65] = 1
            dfs(nx, ny, ans + 1)
            visited[ord(board[nx][ny])-65] = 0    

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 0       
visited = [0] * 26

a, b = map(int, sys.stdin.readline().split()) #2, 4로 들어온다
board = [list(sys.stdin.readline().rstrip()) for _ in range (a)]

visited[ord(board[0][0])-65] = 1
dfs(0, 0, 1)
print(count)