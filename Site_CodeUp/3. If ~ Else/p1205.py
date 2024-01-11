a, b = map(float, input().split())

list_A = [a+b, a-b, a*b, a/b, a**b, b-a, b+a, b*a, b**a]
list_A.sort()
print("%0.6f" %list_A[-1])