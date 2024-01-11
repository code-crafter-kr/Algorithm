a, b = map(int, input().split())

list = [0, 400 ,340, 170, 100, 70]
print("no angry" if list[a]+ list[b] <= 500 else "angry")