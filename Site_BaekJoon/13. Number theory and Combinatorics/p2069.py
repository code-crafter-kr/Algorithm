a, b = map(int, input().split())

if a <= b:
    a , b = b, a

for i in range (b, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
cnt1 = 2
cnt2 = 2

new_a = a
new_b = b

while True:
    if new_a == new_b:
        print(new_a)
        break
    elif new_a < new_b:
        new_a = a * cnt1
        cnt1 += 1
    else:
        new_b = b * cnt2
        cnt2 += 1
