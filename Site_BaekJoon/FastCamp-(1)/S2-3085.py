import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def switch(lst, a, b, c, d):
    
    original = lst[a][b]
    lst[a][b] = lst[c][d]
    lst[c][d] = original
    
    return lst

def check_row(lst, row):
    current_char = lst[row][0]
    temp = 1
    ans = 1
    for i in range(1, n):
        if lst[row][i] == current_char:
            temp += 1
        else:
            current_char = lst[row][i]
            temp = 1
        ans = max(ans, temp)
    return ans

def check_col(lst, col):
    current_char = lst[0][col]
    temp = 1
    ans = 1
    for i in range(1, n):
        if lst[i][col] == current_char:
            temp += 1
        else:
            current_char = lst[i][col]
            temp = 1
        ans = max(ans, temp)

    return ans

ans = 0
n = int(input())
lst = []

for i in range (n):
    temp = list(input().strip())
    lst.append(temp)


for i in range (n):
    for j in range (n):
        try:
            lst = switch(lst, i, j, i, j+1)
            ans = max(ans, check_row(lst, i), check_col(lst, j), check_col(lst, j+1))
            lst = switch(lst, i, j, i, j+1)
        except:
            pass

        try:
            lst = switch(lst, i, j, i+1, j)
            ans = max(ans, check_row(lst, i), check_row(lst, i+1), check_col(lst, j))
            lst = switch(lst, i, j, i+1, j)
        except:
            pass


print(ans)