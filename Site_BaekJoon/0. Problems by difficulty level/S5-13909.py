import math
# 약수의 개수가 짝수면 닫히고.
# 약수의 개수가 홀수면 열리고. => 완전 제곱수

n = int(input())
cnt = 0

standard = 1
while standard ** 2 <= n:
    cnt += 1
    standard += 1

print(cnt)