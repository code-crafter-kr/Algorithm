import sys
sys.stdin = open("input.txt", "r")
w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x_t = t % (w * 2)
y_t = t % (h * 2)

sw_x, sw_y = 1, 1
for i in range (x_t):
    if x == w:
        sw_x = -1
    elif x == 0:
        sw_x = 1

    x += sw_x

for i in range (y_t):
    if y == h:
        sw_y = -1
    elif y == 0:
        sw_y = 1

    y += sw_y

print(x, y)