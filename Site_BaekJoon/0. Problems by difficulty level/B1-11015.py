import sys
sys.stdin = open("input.txt", "r")

def decimal_to_base(decimal_num, base):
    if decimal_num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while decimal_num > 0:
        remainder = decimal_num % base
        result = digits[remainder] + result
        decimal_num //= base
    
    return result


num, base = map(int, input().split())
print(decimal_to_base(num, base))

