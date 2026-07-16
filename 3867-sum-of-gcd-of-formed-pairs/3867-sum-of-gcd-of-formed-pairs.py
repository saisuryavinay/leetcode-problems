class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi = 0
        res = []
        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            res.append(gcd(nums[i],maxi))
        res.sort()
        ans = 0
        n = len(res)
        for i in range(len(res) // 2):
            ans += gcd(res[i],res[n - i - 1])
        return ans