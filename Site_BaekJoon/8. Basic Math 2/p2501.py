n, m = map(int, input().split())

cnt = 0
sw = 0
for i in range (n):
    if n % (i+1) == 0:
        cnt += 1
    if cnt == m:
        print(i+1)
        sw = 1
        break

if sw == 0:
    print(0)