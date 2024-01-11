a,b,c,d = map(int, input().split())

for i in range (0,d-1):
    a = (a * b + c)

print(a)