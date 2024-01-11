# 날짜 유효성 검사기
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for i in range (n):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:8]

    if int(month) < 1 or int(month) > 12:
        print(f"#{i+1} -1")
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            print(f"#{i+1} -1")
        else:
            print(f"#{i+1} {year}/{month}/{day}")
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            print(f"#{i+1} -1")
        else:
            print(f"#{i+1} {year}/{month}/{day}")
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 28:
            print(f"#{i+1} -1")
        else:
            print(f"#{i+1} {year}/{month}/{day}")
    else:
        print(f"#{i+1} -1")

    