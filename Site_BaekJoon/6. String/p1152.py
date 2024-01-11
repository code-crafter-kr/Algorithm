# S = str(input())

# list_S = S.split(" ")
# count = 0
# for i in list_S:
#     if i != "":
#         count = count + 1

# print(count)

S = str(input())
count = 0
list_S = S.split(" ")
for i in range (len(list_S)):
    if list_S[i] != "":
        count = count + 1

print(count)