lst = sorted(list(map(int, input().split())))

if lst[-1] >= lst[0] + lst[1]: #삼각형이 안되는조건
    print((lst[0] + lst[1]) * 2 - 1)
else:
    print(sum(lst))

