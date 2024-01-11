import sys
sys.stdin=open('input.txt','r')

a, b = input().split()
c, d = input().split()
e, f = input().split()

list_A = [a, c, e]
list_B = [b, d, f]

if list_A.count(a) != 2:
    print(a, end = " ")
else:
    if a == c:
        print(e, end = " ")
    else:
        print(c, end = " ")


if list_B.count(b) != 2:
    print(b)
else:
    if b == d:
        print(f)
    else:
        print(d)