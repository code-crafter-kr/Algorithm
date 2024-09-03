import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def isPalindrom(lst):
    if lst == list(reversed(lst)):
        return True    
    else:
        return False

def convert(num, base):
    result = []
    while num > 0:
        remainder = num % base
        result.append(remainder)
        num //= base
    return result

def solve(num):
    for i in range(2,65):
        result = convert(num, i)
        if isPalindrom(result):
            print(1)
            return
    print(0)

n = int(input())
for i in range (n):
    num = int(input())
    solve(num)