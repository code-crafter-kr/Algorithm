a, b, c = input().split()
b, c = map(int, (b,c))

b = ("%d" %b if b > 10 else "0%d" %b)
c = ("%d" %c if c > 99 else "0%d" %c if c > 9 else "00%d" %c) 

print(a+b+c)