import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")

def dfs(y, x):
    if y < 0 or x < 0 or y >= b or x >= a:
        return False

    elif visited[y][x] == 0:
        return False

    elif visited[y][x] == 1:
        visited[y][x] = 0
        dfs(y - 1, x)
        dfs(y , x - 1)
        dfs(y + 1 , x)
        dfs(y , x + 1)
        dfs(y + 1, x + 1)
        dfs(y + 1, x - 1)
        dfs(y - 1, x - 1)
        dfs(y - 1, x + 1)

        return True
    
    return
    


while True:
    a, b = map(int, input().split()) # 1, 1

    if a == b and a == 0:
        break

    else:
        if a > 1:
            visited = [list(map(int, input().split())) for _ in range (b)] # 두 줄

        else:
            visited = [int(input()) for _ in range (b)]

    cnt = 0
    if visited == [0]: # xy가 1 1 일때
        print(cnt)

    elif visited == [1]:
        print(1)

    elif a > 1 and b > 1: #1 1 이상일때
        for yy in range (b):
            for xx in range (a):
                if dfs(yy,xx) == True:
                    cnt += 1
        print(cnt)
