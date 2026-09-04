class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            maxi = nums[0]
            for j in range(1, i + 1):
                maxi = max(maxi, nums[j])

            mini = nums[i]
            for j in range(i + 1, n):
                mini = min(mini, nums[j])
            if maxi - mini <= k:
                return i

        return -1