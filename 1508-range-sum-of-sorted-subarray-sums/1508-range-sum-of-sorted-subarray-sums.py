class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums) + 1):
                res.append(sum(nums[i:j]))
        res.sort()
        ans = []
        for i in range(left-1,right):
            ans.append(res[i])
        return (sum(ans) % MOD)