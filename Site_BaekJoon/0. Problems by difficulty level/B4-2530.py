import sys
sys.stdin = open("input.txt", "r")

a, b, c = map(int, input().split())
t = int(input())

t_min = t // 60
t = t % 60
t_hour = t_min // 60
if t_hour >= 1:
    t_min = t_min % 60

c = c + t
if c >= 60:
    c = c - 60
    b = b + 1

b = b + t_min
if b >= 60:
    b = b - 60
    a = a + 1

a = a + t_hour
if a >= 24:
    a = a % 24

print(a, b, c)