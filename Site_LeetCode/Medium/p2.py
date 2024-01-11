# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    l1_num = 0
    l2_num = 0
    for i in range (len(l1)):
        l1_num += (10**i) * l1[i]
    for j in range (len(l2)):
        l2_num += (10**j) * l2[j]

    sum_result = l1_num + l2_num
    lst = []
    str_result = str(sum_result)[::-1]

    for x in str_result:
        lst.append(x)

    lst = list(map(int, lst))
    return lst


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwoNumbers(l1, l2))