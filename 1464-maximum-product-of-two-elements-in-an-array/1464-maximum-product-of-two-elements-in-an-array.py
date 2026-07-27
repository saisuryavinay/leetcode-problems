class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = sorted(nums, reverse = True)
        maxi1 = ans[0]
        maxi2 = ans[1]
        return (maxi1 - 1) * (maxi2 - 1)