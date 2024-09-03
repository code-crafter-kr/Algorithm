import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range (n):
    h, w, z = map(int, input().split())
    x = z // h # 몇 호실
    y = z % h  # 몇 층
    if y == 0:
        y = h
        x -= 1
    print("%d%02d" %(y, x+1))

# for i in lst:
#     print(*i)

# T = int(input())

# for _ in range(T):
#     H, W, N = map(int, input().split())
    
#     floor = N % H
#     room = N // H + 1
    
#     if floor == 0:
#         floor = H
#         room -= 1
    
#     print(f"{floor}{room:02d}")