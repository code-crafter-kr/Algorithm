n = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())

result = 0
for i in lst:
    if i == 0:
        continue
    elif i <= t:
        result += 1
    else:
        if i % t == 0:
            result += (i // t)
        else:
            result += 1 + (i // t)
print(result)
print(n // p, n % p)