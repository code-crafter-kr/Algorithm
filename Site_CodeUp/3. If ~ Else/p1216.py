a, b, c = map(int, input().split())

print("advertise" if b-c > a else "do not advertise" if b-c < a else "does not matter")