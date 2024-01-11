# 비밀번호 시도 횟수

import sys
sys.stdin = open("input.txt", "r")

p, k = map(int, input().split())
print(p - k + 1)