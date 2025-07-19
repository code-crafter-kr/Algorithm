from collections import deque
import sys


lst = deque()
for i in range (int(sys.stdin.readline())):
    x = sys.stdin.readline()
    try:
        x = int(x)
    except:
        x, y = map(int, x.split())

    
    if x == 1:
        lst.appendleft(x)
    elif x == 2:
        lst.append(x)
    elif x == 3:
        if lst:
            print(lst.popleft())
        else:
            print(-1)
    elif x == 4:
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif x == 5:
        print(len(lst))
    elif x == 6:
        if lst:
            print(0)
        else:
            print(1)
    elif x == 7:
        if lst:
            print(lst[0])
        else:
            print(-1)
    else:
        if lst:
            print(lst[-1])
            print(-1)

