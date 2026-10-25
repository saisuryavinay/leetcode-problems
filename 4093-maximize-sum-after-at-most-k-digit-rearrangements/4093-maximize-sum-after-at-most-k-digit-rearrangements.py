class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        ans = []
        for i in range(len(nums)):
            s = sorted(str(nums[i]),reverse = True)
            val = int("".join(s))
            ans.append(val - nums[i])
        ans.sort(reverse = True)

        for i in range(min(k,len(nums))):
            nums[i] += ans[i]
        return sum(nums)