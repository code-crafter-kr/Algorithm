import sys
import math
# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

# 이분탐색알고리즘 lst에서 가장 가까운 작은수 찾기
def binary_search(lst, n):
    left, right = 0, len(lst) - 1
    best_idx = -1  # 가장 가까운 작은 수의 인덱스 저장

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] <= n:
            best_idx = mid  # 현재 mid 값이 유효하므로 저장
            left = mid + 1  # 더 큰 값 탐색
        else:
            right = mid - 1  # 더 작은 값 탐색

    return best_idx

n = int(sys.stdin.readline())

#에라토스 테네스의 체체
a = [False,False] + [True]*(1000000-1)
primes=[]
for i in range(2, 1000000 + 1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, 1000000+1, i):
        a[j] = False

for i in range (n):
    x = int(sys.stdin.readline())
    cnt = 0
    left = 0
    right = binary_search(primes, x)

    while left <= right:
        if primes[left] + primes[right] == x:
            cnt += 1
            left += 1
            right -= 1

        elif primes[left] + primes[right] > x:
            right -= 1
        
        elif primes[left] + primes[right] < x:
            left += 1

    print(cnt)
