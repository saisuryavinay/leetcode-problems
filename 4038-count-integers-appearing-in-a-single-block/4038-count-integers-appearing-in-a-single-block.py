class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans = {}
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                ans[nums[i]] = ans.get(nums[i],0) + 1

        res = 0
        for x in ans:
            if ans[x] == 1:
                res += 1
        return res