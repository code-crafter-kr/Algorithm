import sys

sys.stdin = open("input.txt", "r")

m, n = map(int, input().split())

lst = [0] + [x for x in range(1, m+1)]

for _ in range (n):
    a, b = map(int, input().split())
    reversed_part = lst[a:b+1][::-1]
    rest_1 = lst[:a]                 
    rest_2 = lst[b+1:]                 
    lst = rest_1 + reversed_part + rest_2 

print(*lst[1:])