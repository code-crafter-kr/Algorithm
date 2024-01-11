a, b = map(int, input().split())

for ii in range (b):

    for jj in range (a-1):
        print(" "*jj, end = "")
        print("*")
    for jj in range (a-1, -1, -1):
        print(" "*jj, end = "")
        print("*")