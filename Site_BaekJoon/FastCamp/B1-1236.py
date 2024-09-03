import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())

lst = []
cumulative_col_guard = [0 for _ in range (m)]
cumulative_row_guard = [0 for _ in range (n)]
for i in range (n): 
    temp = list(input())
    if "X" in temp:
        cumulative_row_guard[i] = 1
    for j in range (m):
        if temp[j] == "X" and cumulative_col_guard[j] == 0:
            cumulative_col_guard[j] = 1
    lst.append(temp)

print(max(cumulative_col_guard.count(0), cumulative_row_guard.count(0))) 