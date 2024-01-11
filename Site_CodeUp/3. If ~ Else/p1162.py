a, b, c = map(int, input().split())

print("대박" if (a - b + c)%10 == 0 else "그럭저럭")