class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        cnt = 0
        len1 = 0
        for i in range(len(nums)):
            if minK <= nums[i] <= maxK:
                len1 += 1
                cnt += len1
            else:
                len1 = 0
        return cnt