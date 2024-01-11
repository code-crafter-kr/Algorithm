a = input()
b = input()
c = input()
a,b,c = map(list, (a,b,c))

print("good" if (a[-1] == b[0]) and (b[-1] == c[0]) and (c[-1] == a[0]) else "bad")

