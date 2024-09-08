a, b = map(int, input().split())
c = int(input())
n = int(input())


if ((c-a) * 100) - b < 0:
    print(0, end = "")
else:
    print(1, end = "")
