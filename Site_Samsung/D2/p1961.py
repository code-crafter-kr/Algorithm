import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

def rotate(lst, n):
    new_lst = []

    for i in range(n):
        temp = ""
        for j in range(n-1, -1, -1):
            temp += str(lst[j][i])
        new_lst.append(temp)
    return new_lst


for _ in range(T):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    
    rotate_90 = rotate(lst, n)
    rotate_180 = rotate(rotate_90, n)
    rotate_270 = rotate(rotate_180, n)
    print(f"#{_ + 1}")
    for x in range (n):
        print(rotate_90[x], rotate_180[x], rotate_270[x])