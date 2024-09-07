import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k, b = map(int, input().split())

lst = [1 for i in range (n)]
for i in range (b):
    broken = int(input())
    lst[broken - 1] = 0

cumulative_sum = [sum(lst[:k])]
temp = cumulative_sum[0]
for i in range (k, n):
    temp -= lst[i-k]
    temp += lst[i]
    cumulative_sum.append(temp)

result = max(cumulative_sum)
if k - result >= 0:
    print(k - result, end = "")
else:
    print(0, end = "")
