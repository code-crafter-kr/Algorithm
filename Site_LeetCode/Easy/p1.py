class Solution(object):
    def twoSum(self, nums, target):
        new_lst = sorted(nums)
        idx_front = 0
        idx_back = len(nums)-1
        while True:
            print(idx_front, idx_back)
            if target == (new_lst[idx_front] + new_lst[idx_back]):
                a = nums.index(new_lst[idx_front])
                nums[a] = 1.1
                b = nums.index(new_lst[idx_back])

                return [a, b]

            elif target <= (new_lst[idx_front] + new_lst[idx_back]):
                idx_back -= 1
            else:
                idx_front += 1

