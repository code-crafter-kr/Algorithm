from re import I


a, b = map(int, input().split())
list_A = [i for i in range(a, b+1)]
x = 0
for i in list_A:
    if i % 2 == 0:
        x -= i
    else:
        x += i
print(x)