x, y, w, h = input().split()
x, y, w, h = int(x), int(y), int(w), int(h)
A = w - x # x축
if A > x:
    A = x
B = h - y # y축
if B > y:
    B = y
if A < B:
    print(A)
else:
    print(B)