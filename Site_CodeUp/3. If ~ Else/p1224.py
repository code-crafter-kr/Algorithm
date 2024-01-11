a, b, c, d = map(int, input().split())

print(">" if a*d > b*c else "=" if a*d == b*c else "<")