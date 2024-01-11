a, b, c = input().split()
c = int(c)
c = ("0%d" %c if c < 10 else "%d" %c)

print(a+b+c)