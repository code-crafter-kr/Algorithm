import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = input()
lst = sorted(list(map(int, input().split())))
key = int(input())

#base case
if len(lst) == 1:
    if key == lst[0]:
        print(1)
    else:
        print(0)
else:
    start = 0
    end = len(lst) - 1
    ans = 0
    while True:
        if start == end:#완전히 맞물리면 끝
            break
        else:
            if lst[start] + lst[end] == key:
                ans += 1
                start += 1
            elif lst[start] + lst[end] > key:
                end -=1
            else:
                start += 1

    print(ans)