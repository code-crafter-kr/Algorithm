import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
cumulative_sum = []
temp = sum(lst[:m])
cumulative_sum.append(temp)

for i in range (m, n):
    temp += lst[i]
    temp -= lst[i-m]
    cumulative_sum.append(temp)

print(max(cumulative_sum), end = "")