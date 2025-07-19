import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(map(int, input().split()))      # 오름차순 정렬

def get_total(height):
    result = 0
    for i in lst:
        if i < height:
            continue
        else:
            result += i - height
    return result


left = 0
right = max(lst)
result = -1

while left <= right:
    mid = (left + right) // 2

    if get_total(mid) >= m:
        result = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(result)