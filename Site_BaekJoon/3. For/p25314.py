import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
n = n // 4

for i in range(n):
    print("long", end = " ")
print("int")