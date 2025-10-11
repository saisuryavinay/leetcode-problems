class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        count = 0
        count1 = 0
        for i in range(n):
            if nums[i] != 0:
                res.append(nums[i])
        for i in range(len(res)):
            if res[i] < 0:
                count+=1
            elif res[i] > 0:
                count1+=1
        return max(count,count1)
        print(res)