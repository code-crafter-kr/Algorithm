a, b= map(int, (input().split()))

print("%d*%d=%d" %(a,b//a,b) if b % a == 0 else "%d*%d=%d" %(b,a//b,a) if a % b == 0 else "none")