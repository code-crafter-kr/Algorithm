# 369 게임

import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

n = input()

for i in range(1, int(n)+1):
    num = str(i)
    count = Counter(num)
    time = count['3'] + count['6'] + count['9']
    if time == 0:
        print(i, end=' ')
    else:
        print('-'*time, end=' ')
    