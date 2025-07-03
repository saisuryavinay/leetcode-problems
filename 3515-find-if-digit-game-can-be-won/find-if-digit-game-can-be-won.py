import math
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_lst = []
        double_digit_lst = []
        n = len(nums)
        for i in range(n):
            if nums[i]<=9:
                single_digit_lst.append(nums[i])
            elif nums[i]>=10:
                double_digit_lst.append(nums[i])
        # print(single_digit_lst)
        # print(double_digit_lst)
        ans1 = sum(single_digit_lst)
        ans2 = sum(double_digit_lst)
        # print(ans1)
        # print(ans2)
        if ans1>ans2 or ans2>ans1:
            return True
        return False