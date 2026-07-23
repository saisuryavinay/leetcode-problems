class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        ans = 0
        for num in nums:
            ans |= num
        return ans + 1