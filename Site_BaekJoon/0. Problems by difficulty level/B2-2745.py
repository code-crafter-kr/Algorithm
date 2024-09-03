import sys
sys.stdin = open("input.txt", "r")

s1, base = input().split()
s1 = s1[::-1]
cnt = 0
result = 0
for alpha in s1:
    base_num = int(base) ** cnt
    if alpha.isalpha():
        result += (ord(alpha) - 55) * base_num
    else:
        result += int(alpha) * base_num
    cnt += 1

print(result)
