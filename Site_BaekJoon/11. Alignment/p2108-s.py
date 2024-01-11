import sys
from collections import Counter

n = int(sys.stdin.readline())

list_A = []
for i in range(n):
    list_A.append(int(sys.stdin.readline()))

print(round(sum(list_A)/n))

list_A.sort()
print(list_A[int(n//2)])

cnt = Counter(list_A).most_common(2)

if len(list_A) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])


print(max(list_A) - min(list_A))