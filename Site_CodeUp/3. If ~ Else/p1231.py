a = input()
s = -1

for i in ["+", "-", "*", "/"]:
    b = a.split(i)
    s += 1
    if len(b) == 2:
        b = list(map(int, b))
        if s == 0:
            print(b[0]+b[1])
        elif s == 1:
            print(b[0]-b[1])
        elif s == 2:
            print(b[0]*b[1])
        else:
            b = list(map(float, b))
            print("%0.2f" %(b[0]/b[1]))