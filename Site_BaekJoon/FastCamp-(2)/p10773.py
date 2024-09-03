import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
ans = deque()
for i in range (n):
    x = int(input())
    if x == 0 and len(ans) == 0:
        continue
    elif x == 0:
        ans.pop()
    else:
        ans.append(x)
print(sum(ans), end = "")