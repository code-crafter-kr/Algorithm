import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())

lst = [["." for _ in range (n)] for _ in range (n)]
s = input().strip()

def move(y, x, alpha):
    if alpha == "D":
        y += 1
    elif alpha == "U":
        y -= 1
    elif alpha == "R":
        x += 1
    elif alpha == "L":
        x -= 1
    
    if 0 <= x < n and 0 <= y < n:
        return y, x
    else:
        return -1, -1
    
def shape(y, x):
    current_shape = lst[y][x]
    if current_shape == "+":
        pass
    elif (current_shape == "|" and (i == "R" or i == "L")) or (current_shape == "-" and (i == "U" or i == "D")):
        lst[y][x] = "+"
    elif i == "U" or i == "D":
        lst[y][x] = "|"
    else:
        lst[y][x] = "-"

current_x = 0
current_y = 0
for i in s:
    new_y, new_x = move(current_y, current_x, i)
    if new_x == -1:
        continue
    else:
        shape(current_y, current_x)

        if i == "U":
            shape(current_y - 1, current_x)
        elif i == "D":
            shape(current_y + 1, current_x)
        elif i == "L":
            shape(current_y, current_x - 1)
        else:
            shape(current_y, current_x + 1)

        current_y, current_x = new_y, new_x

for i in range (len(lst)):
    if i == len(lst) - 1:
        print("".join(lst[i]), end ="")
    else:
        print("".join(lst[i]))
