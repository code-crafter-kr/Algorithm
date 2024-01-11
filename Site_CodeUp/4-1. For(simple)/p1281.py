# a, b = map(int, input().split())
# list_A = [i for i in range(a, b+1)]
# x = 0
# d = 0
# for i in list_A:
#     if i % 2 == 0:
#         x -= i
#         print("%d" %-i, end = "")
#         d = d + 1
#     else:
#         if d == 0:
#             x += i
#             print("%d" %i, end = "")
#             d = d +1
#         else:
#             x += i
#             print("+%d" %i, end="")

# print("=%d" %x)

a, b = map(int, input().split())
list_A = [i for i in range(a, b+1)]
list_B = []
x = 0
for i in list_A:
    if i % 2 == 0:
        x-= i
        list_B.append("-%d" %i)
    else:
        x+= i
        list_B.append("+%d" %i)

if a % 2 == 1:
    list_B[0] = "%d" %a
print(''.join(list_B), end ="")
print("=%d" %x)