a, b, c = map(int, input().split())
list = [a,b,c]

list.sort()
for i in range (0,3):
    print(list[i], end = " ")