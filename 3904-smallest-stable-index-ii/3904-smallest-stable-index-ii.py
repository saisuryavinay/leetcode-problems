class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        res = [0] * n
        mini = float('inf')
        for i in range(n - 1, -1, -1):
            mini = min(mini, nums[i])
            res[i] = mini
        print(res)
        mx = nums[0]
        for i in range(n):
            mx = max(mx, nums[i])
            score = mx - res[i]
            if score <= k:
                return i
 
        return -1