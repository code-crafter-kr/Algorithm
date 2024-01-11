a,b = map(int, input().split())

if b <= 2:
    print(113 - (a//10000))

else:
    print(13 - a//10000)