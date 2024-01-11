n = int(input())

def ha_count(n):
    if n == 1:
        return 1
    else:
        return ha_count(n-1)*2 + 1

print(ha_count(n))

def ha_path(n, a, b):
    if n > 1:
        ha_path(n-1, a, 6-a-b)
                     
    print(a, b)

    if n > 1:
        ha_path(n-1, 6-a-b, b)

ha_path(n,1,3)                             