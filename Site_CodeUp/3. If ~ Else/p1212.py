a, b, c = map(int, input().split())
list = [a,b,c]
list.sort()
print("yes" if list[2] < list[0]+list[1] else "no")