import sys
sys.setrecursionlimit(10**9)
n = int(input())

def dfs(y, x):
    if y < 0 or x < 0 or y >= b or x >= a:
        return False

    elif visited[y][x] == 0:
        return False

    elif visited[y][x] == 1:
        visited[y][x] = 0
        dfs(y-1, x)
        dfs(y , x -1)
        dfs(y+1 , x)
        dfs(y , x + 1)
        return True
    
    return
    

for i in range (n):
    cnt = 0
    a, b, c = map(int, input().split()) # a = x = 10, b = y = 8
    visited = [[0]*a  for _ in range(b)]

    for ii in range (c):
        x, y = map(int, input().split())
        visited[y][x] = 1

    for yy in range (b):
        for xx in range (a):
            if dfs(yy,xx) == True:
                cnt += 1
    print(cnt)