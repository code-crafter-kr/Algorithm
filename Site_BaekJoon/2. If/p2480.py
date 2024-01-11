a, b, c = map(int, input().split())

list_A = [a, b ,c]
list_A.sort()

if a == b == c:
    print(10000 + a*1000)

elif a != b and a != c and b !=c:
    print(100*list_A[-1])

else:
    print(1000 + 100*list_A[1])