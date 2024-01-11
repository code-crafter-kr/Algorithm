a , b = map(int, input().split())

print(a if b >=30 else a-1 if a-1 != -1 else "23", end = " ")
print(b-30 if b >= 30 else b + 60 - 30)
