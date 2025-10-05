class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res1 = []
        res2 = []
        for i in range(len(nums)):
            if i%2 ==0:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        print(res1)
        print(res2)
        n = sum(res1)
        m = sum(res2)
        return n-m