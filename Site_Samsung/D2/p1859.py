# 백만장자 프로젝트

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    x = int(input()) # not use = len(lst)
    lst = list(map(int, input().split()))
    # result should be long type
    result = 0
    
    # reverse list
    day = 0
    for j in range(len(lst)-1, -1, -1):
        # compare today and yesterday
        day = max(day, lst[j])
        if j != 0: # don't compare the first day
            today = lst[j-1]
            if today < day:
                result += day - today
    print(f'#{i+1} {result}')