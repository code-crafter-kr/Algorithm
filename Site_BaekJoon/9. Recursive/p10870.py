def fibo(n):
    if n == 2: # 종료조건으로
        return 1
    elif n == 1: # n이 1일때 리턴값이 0
        return 0
    else:
        return fibo(n-1) + fibo(n-2)
    
a = int(input())
print(fibo(a+1))