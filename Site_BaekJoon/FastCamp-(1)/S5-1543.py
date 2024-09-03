s1 = input()
s2 = input()

ans = 0
while True:
    try:
        s1 = s1[s1.index(s2) + len(s2): ]
        ans += 1
    except:
        print(ans)
        break