for i in range (1,10):
    print("2 x %d = %2d\t3 x %d = %2d\t4 x %d = %2d\t5 x %d = %2d" %(i, i*2, i, i*3, i, i*4, i, i*5), end="")
    print()

for i in range (1,10):
    for j in range (2,6):
        print("%d x %d = %2d\t" %(j, i, i*j), end = "")
    print()