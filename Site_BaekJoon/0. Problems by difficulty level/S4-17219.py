import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n, m = map(int, input().split())

lst = dict()
for i in range(n):
    a, b = input().split()
    lst[a] = b

for j in range(m):
    command = input().strip()
    print(lst[command])