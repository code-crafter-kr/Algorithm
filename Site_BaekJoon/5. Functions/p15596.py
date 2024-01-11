# 함수 문제 '정수 N개의 합
a = []
a = list(map(int, a))

def solve(a):
    result =0
    for i in range (len(a)):
        result = result + a[i]
    return result