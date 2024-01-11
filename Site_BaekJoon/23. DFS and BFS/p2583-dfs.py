import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt", "r")

def dfs(y, x):
    global cnt
    if y < 0 or x < 0 or y >= N or x >= M:
        return False

    elif board[y][x] == 1:
        return False

    elif board[y][x] == 0:
        board[y][x] = 1
        cnt += 1
        dfs(y-1, x)
        dfs(y , x -1)
        dfs(y+1 , x)
        dfs(y , x + 1)
        return True
    
    return

#board 전처리
N, M, K = map(int, sys.stdin.readline().split())
board_p = [0] * (M)
board = [board_p.copy() for _ in range (N)]

for _ in range (K):
    a, b, c, d = map(int, sys.stdin.readline().split()) # 0 2 4 4 >> 2 - > 4 / 0 > 4
    for ii in range (b, d):
        for jj in range (a, c):
            board[ii][jj] = 1 #막힌곳 표시

# dfs 실행
a = 0
cnt_lst = []
for xx in range (N):
    for yy in range (M):
        cnt = 0
        if dfs(xx, yy) == True:
            cnt_lst.append(cnt) #영역의 넓이 저장
            a += 1 #영역의 개수 저장
            
#출력
cnt_lst.sort() #오름차순을 위한 sort()
print(a)
print(* cnt_lst)