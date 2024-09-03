import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input()) # 총 학생의 수
T = int(input()) # 스태프의 수

lst = []
my_dict = {}
all_scores = []

idx = 0
ans_dict = {}

for i in range (T):
    staff, vote = input().split()
    vote = int(vote)
    if vote / n < 0.05:
        continue
    ans_dict[staff] = 0
    lst.append([staff, vote])
    for j in range (1, 14):
        my_dict[lst[idx][1] / j] = staff
        all_scores.append(lst[idx][1] / j)
    idx += 1
all_scores.sort(reverse=True)

cnt = 0

for x in all_scores:
    if cnt == 14:
        break
    ans_dict[my_dict[x]] += 1
    cnt += 1

ans = sorted(list(ans_dict))
for a in range (len(ans)):
    if a == len(ans) - 1:
        print(ans[a], ans_dict[ans[a]], end = "")
    else:
        print(ans[a], ans_dict[ans[a]])