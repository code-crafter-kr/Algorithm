import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")

def dfs(y, x, z):
    if y < 0 or x < 0 or y >= n or x >= n:
        return False

    elif visited[y][x] < z:
        return False

    elif visited[y][x] >= z:
        visited[y][x] = 0
        dfs(y - 1, x, z)
        dfs(y , x - 1, z)
        dfs(y + 1 , x, z)
        dfs(y , x + 1, z)
        return True 
    return

n = int(input())

temp = []
visited2 = [list(map(int, input().split())) for _ in range (n)]

for i in range (1, 101):
    visited = []
    for j in visited2:
        visited.append(j.copy())
    cnt = 0

    for ii in range (n):
        for jj in range (n):
            if dfs(ii, jj , i) == True:
                cnt += 1
    temp.append(cnt)

print(max(temp))