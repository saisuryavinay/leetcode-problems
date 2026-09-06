class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        half = n // 2
        tot = sum(nums)
        first = sum(nums[:half])
        
        for i in range(n):
            
            second = tot - first

            if first > second:
                ans += 1

            first -= nums[i]
            if i+ half  < n:
                first += nums[i + half]
            else:
                first += nums[i + half - n]
        return ans