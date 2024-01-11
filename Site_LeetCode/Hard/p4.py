def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    lst = []
    idx_num1 = 0
    idx_num2 = 0

    if (m + n) % 2 == 0:
        median_type = True
    else:
        median_type = False

    end = int((m + n) / 2) + 1

    for i in range (end):
        if idx_num1 == n:
            lst = lst + nums2[idx_num2:(end - idx_num1)]
            if median_type == True:
                return (lst[-1] + lst[-2]) / 2.0
            else:
                return float(lst[end-1])

        elif idx_num2 == m:
            lst = lst + nums1[idx_num1:(end - idx_num2)]
            if median_type == True:
                return (lst[-1] + lst[-2]) / 2.0
            else:
                return float(lst[end-1])

        else:
            if nums1[idx_num1] <= nums2[idx_num2]:
                lst.append(nums1[idx_num1])
                idx_num1 += 1
            else:
                lst.append(nums2[idx_num2])
                idx_num2 += 1

        if i == end-1:
            if median_type == True:
                return (lst[-1] + lst[-2]) / 2.0
            else:
                return float(lst[end-1])



print(findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1]))    