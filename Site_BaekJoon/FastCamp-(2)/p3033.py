import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())
s = input()

# 일단 중복되는 부분문자열 ... 을 다 구함

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # 현재 지수가 홀수이면
            result = (result * base) % mod
        exp = exp >> 1  # 지수를 절반으로 줄임
        base = (base * base) % mod  # 기저를 제곱
    return result

mod = 1e9 + 7

string_list = []
if n == 1 or n == 2: #절대 중복문자열이 등장할 수 없는 경우의 수
    print(0)
else:
    value = 0
    for i in range (2):
        value *= 31
        value += ord(s[i]) - ord('a') + 1
    initial_list = [value]

    for i in range (2, n):
        value = initial_list[-1]
        value *= 31
        value %= mod
        value += ord(s[i]) - ord('a') + 1
        value %= mod
        initial_list.append(value)

def solve():
    for i in range (n-1, 1, -1): # 가장 긴 문자열부터 검사 시작.. n-1는 10에서 2까지
        
        initial = initial_list[i - 2]
        sub_string_hash = initial
        exist = {initial : True}
        for x in range (1, n - i + 1):
            mod_p = mod_exp(31, i-1, mod)
            largest_alpha = ord(s[x-1]) - ord('a') + 1
            sub_string_hash -= (largest_alpha * mod_p) % mod
            if sub_string_hash < 0:
                sub_string_hash += mod
            sub_string_hash %= mod

            sub_string_hash *= 31
            sub_string_hash %= mod

            sub_string_hash += ord(s[i + x - 1]) - ord('a') + 1
            sub_string_hash %= mod
            try:
                exist[sub_string_hash]
                print(i)
                print(exist)
                return
            except:
                exist[sub_string_hash] = True

    print(0)

solve()