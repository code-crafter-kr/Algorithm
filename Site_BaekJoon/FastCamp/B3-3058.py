import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
for i in range (n):
    temp = list(map(int, input().split()))
    result = 0
    minimum = 101
    for x in temp:
        if x % 2 == 0:
            minimum = min(minimum, x)
            result += x
    print(result, minimum)