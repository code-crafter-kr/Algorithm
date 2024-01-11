a, b = map(int, input().split())
s = int(input())
x = (b + s) % 60
y = (b + s) //60
a = a + y

a = a if a < 24 else a - 24
print(a, x)