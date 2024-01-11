# 문자열 문제 '숫자의 합'

N = int(input())
B = input() #54321
C = 0
# B[0] + B[1] ... B[4]

for i in B:
    C = C + int(i)

print(C)


