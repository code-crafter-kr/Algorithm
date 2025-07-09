s = input()

result = 0

for i in range (len(s)):
    if s[i] == "*":
        idx = i
        continue
    if i % 2 == 0:
        result += int(s[i])
    else:
        result += int(s[i]) * 3



if idx % 2 == 0:
    for i in range(0, 10):
        if ((result + i) % 10) == 0:
            print(i)
            break
else:
    for i in range(0, 10):
        if ((result + i * 3) % 10) == 0:
            print(i)
            break


