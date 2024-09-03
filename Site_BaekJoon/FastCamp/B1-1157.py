s = input().upper()
my_dict = {}

for i in s:
    try:
        my_dict[i] += 1
    except:
        my_dict[i] = 1

sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True )
if len(sorted_dict) == 1:
    print(sorted_dict[0][0])
elif sorted_dict[0][1] == sorted_dict[1][1]:
    print("?")
else:
    print(sorted_dict[0][0])