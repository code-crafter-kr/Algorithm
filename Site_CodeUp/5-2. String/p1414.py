N = input()
x = 0
y = 0
z = 0
for i in (N):
    if i == "c" or i == "C":
        x = x + 1
        z = z + 1

    else:
        z = 0

    if z == 1:
        pass

    elif z > 1:
        y = y + 1

print(x,y)