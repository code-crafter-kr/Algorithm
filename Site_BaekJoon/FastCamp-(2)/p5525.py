import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
m = int(input())
x = input()

mod = 1e9 + 7 # 10억 7로 나누기
po = [0] * m
po[0] = 1
for i in range (1, m):
    po[i] = po[i-1] * 31 % mod

target = "I"
for i in range (n):
    target += "OI"

target_length = len(target)
target_value = 0
word_value = 0
result = 0

for t in range (target_length):
    target_value *= 31
    target_value %= mod
    target_value += ord(target[t]) - ord('A') + 1
    target_value %= mod
    
    word_value *= 31
    word_value %= mod
    word_value += ord(x[t]) - ord('A') + 1
    word_value %= mod

for i in range (0, m - target_length + 1):
    if word_value == target_value:
        result += 1
    
    largest_alpha = ord(x[i]) - ord('A') + 1
    word_value += mod - largest_alpha * po[target_length-1] % mod
    word_value %= mod
    word_value *= 31
    word_value %= mod

    if i + target_length < m:
        word_value += ord(x[i + target_length]) - ord('A') + 1
        word_value %= mod

print(result)