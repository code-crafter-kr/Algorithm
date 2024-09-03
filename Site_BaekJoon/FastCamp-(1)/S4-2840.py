import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def check_duplication(lst):
    for i in lst:
        if i != "?":
            cnt = lst.count(i)
            if cnt >= 2:
                return False
    return True

n, m = map(int, input().split())
lst = ["?" for _ in range (n)]

current_pos = 0
sw = 0

for i in range (m):
    change, alpha = input().split()
    change = int(change)
    new_pos = (current_pos - change) % n

    if lst[new_pos] == "?":
        lst[new_pos] = alpha
    else:
        if lst[new_pos] != alpha:
            print("!", end = "")
            sw = 1
            break
    current_pos = new_pos

if sw == 0:
    if not check_duplication(lst):
        print("!", end = "")
    else:
        ans_lst = lst[new_pos :] + lst[: new_pos]
        print("".join(ans_lst), end = "")
