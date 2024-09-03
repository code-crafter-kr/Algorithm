import sys
sys.stdin = open("input.txt", "r")
n = int(input())

for i in range (n):
    s = input().split()
    t, temp = s[0], list(map(int, s[1:]))
    ans = 0
    lst = []
    # base case
    for j in temp:
        sw = 0
        if lst == []:
            lst.append(j)
            sw = 1
        for x in range (len(lst)):
            if lst[x] > j: #이게 Sequential Search ... -> If I modify it as binary search..
                ans += len(lst) - x
                lst.insert(x, j)
                sw = 1
                break
        if sw == 0:
            lst.append(j)

    print(t, ans)

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # 요소를 찾음
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 요소를 찾지 못함

