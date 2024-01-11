a, b, c = map(int, input().split())
x = 0
for i in range (0,a):
    for j in range (0,b):
        for z in range (0,c):
            print(i, j, z)
            x += 1
print(x)
