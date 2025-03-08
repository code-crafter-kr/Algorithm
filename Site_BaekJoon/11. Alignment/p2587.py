import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

lst = []
avg = 0

for i in range (5):
    num = int(input())
    lst.append(num)

lst.sort()
print(int(sum(lst) / 5))
print(lst[2], end = "")