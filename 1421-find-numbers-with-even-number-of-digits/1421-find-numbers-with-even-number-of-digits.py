class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            c = 0
            while nums[i]>0:
                c+=1
                nums[i]//=10
            if c %2 ==0:
                ans+=1
        return ans