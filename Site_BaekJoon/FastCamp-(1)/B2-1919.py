s1 = input()
s2 = input()

s1_dict = {}
result = 0
for i in s1:
    try:
        s1_dict[i] += 1
    except:
        s1_dict[i] = 1

for j in s2:
    try:
        s1_dict[j] -= 1
    except:
        result += 1

for key, value in s1_dict.items():
    if value < 0:
        value = value * -1
    result += value

print(result)
