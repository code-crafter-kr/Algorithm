lst = list(map(int, input().split()))

st = "112228"

for i in range (len(st)):
    print(int(st[i]) - lst[i], end = " ")