class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(k):
            if i < mul - 1:
                ans += nums[i] * (mul - i)
            else:
                ans += nums[i]
        return ans