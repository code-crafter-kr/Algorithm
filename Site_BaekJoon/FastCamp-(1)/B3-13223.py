import sys
sys.stdin = open("input.txt", "r")
s1, s2, s3 = map(int, input().split(":"))
x1, x2, x3 = map(int, input().split(":"))
total_s = s1*3600 + s2*60 + s3
total_x = x1*3600 + x2*60 + x3
if total_x <= total_s:
    total_x += 24*3600

result = total_x - total_s
h = result // 3600
m = result % 3600 // 60
s = result % 60
print("%02d:%02d:%02d" % (h, m, s))