import math

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0 or x == 1:
        print(2)
        continue
    while True:
        if is_prime_number(x) == True:
            print(x)
            break
        else:
            x += 1
            continue