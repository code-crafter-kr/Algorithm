import sys
sys.stdin = open("input.txt", "r")

n = int(input())
if n == 1:
    input()
    print(0)
else:
    max_y = -100001
    max_x = -100001
    min_x = 100001
    min_y = 100001

    for i in range (n):
        temp = list(map(int, input().split()))
        max_x = max(max_x, temp[0])
        max_y = max(max_y, temp[1])
        min_x = min(min_x, temp[0])
        min_y = min(min_y, temp[1])
    
    print((max_x - min_x) * (max_y - min_y))
    