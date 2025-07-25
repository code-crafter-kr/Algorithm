import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())
s = input()

# 일단 중복되는 부분문자열 ... 을 다 구함

temp_exist = {}
mod_p = [0] * n
mod_p[0] = 1
mod = 1e9 + 7
for i in range (1, n-1):
    mod_p[i] = mod_p[i-1] * 31 % mod


if n == 1 or n == 2: #절대 중복문자열이 등장할 수 없는 경우의 수
    print(0)
else:
    value = 0
    for i in range (2):
        value *= 31
        value += ord(s[i]) - ord('a') + 1
    initial_list = [value]

    for i in range (2, n-1):
        value = initial_list[-1]
        value *= 31
        value %= mod
        value += ord(s[i]) - ord('a') + 1
        value %= mod
        initial_list.append(value)

print(initial_list)
def solve():
    for i in range (n-2, 1, -1):
        initial = initial_list[i - 1]
        sub_string_hash = initial
        print(i, sub_string_hash)

        for x in range (1, n - i + 1):
            sub_string = s[x : i + x]
            largest_alpha = ord(s[x-1]) - ord('a') + 1
            sub_string_hash += mod - largest_alpha * mod_p[i-1] % mod
            sub_string_hash %= mod

            sub_string_hash *= 31
            sub_string_hash %= mod

            sub_string_hash += ord(s[i + x - 1]) - ord('a') + 1
            sub_string_hash %= mod
            print(sub_string, sub_string_hash)

            if sub_string_hash == initial:
                print(i)
                return

    print(0)

solve()