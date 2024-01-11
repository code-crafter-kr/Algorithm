import sys
sys.stdin = open('input.txt', 'r')

total_price = int(input())

n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a * b

if sum == total_price:
    print("Yes")
else:
    print("No")