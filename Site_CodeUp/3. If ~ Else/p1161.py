a,b = map(int, input().split())

c = "홀수" if a % 2 == 1 else "짝수"
d = "홀수" if b % 2 == 1 else "짝수"

x = "짝수" if c ==d else "홀수"

print("%s+%s=%s" %(c, d, x))