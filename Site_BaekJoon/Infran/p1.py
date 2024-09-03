s_stirng = input()
s_char = input()
s_char = s_char.lower()
cnt = 1
for i in s_stirng:
    if i.lower() == s_char:
        cnt +=1

print(cnt)