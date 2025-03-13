import sys
n = int(sys.stdin.readline())
lst = []
for i in range (n):
    x = sys.stdin.readline()

    try:
        x = int(x)
    except:
        x, y = x.split()
        x, y = int(x), int(y)

    if x == 1:
        lst.append(y)
    elif x == 2:
        try:
            print(lst.pop())
        except:
            print(-1)
    elif x == 3:
        print(len(lst))
    elif x == 4:
        print(1 if len(lst) == 0 else 0)
    else:
        try:
            print(lst[-1])
        except:
            print(-1)