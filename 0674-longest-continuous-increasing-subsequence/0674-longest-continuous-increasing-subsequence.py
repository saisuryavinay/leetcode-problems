class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)-1
        count = 1
        ans = count
        for i in range(n):
            if nums[i] < nums[i+1]:
                count+=1
            else:
                count=1
            ans = max(ans,count)
        return ans