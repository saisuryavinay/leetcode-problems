class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            c = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    c+=1
            res.append(c)
        return res