n = int(input())
s = input()

result = 0
idx = 0
for i in s:
    n = ord(i) - 96
    x = 31 ** idx
    idx += 1

    result += x * n
    result %= 1234567891

print(result)