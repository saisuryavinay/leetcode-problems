class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        res = []
        for x in nums:
            if lower <= x <= upper:
                res.append(x)
        num = list(set(res))
        num.sort()
        ans = []
        start = lower
        for x in num:
            if start < x:
                ans.append([start,x - 1])

            start = x + 1
        if start <= upper:
            ans.append([start,upper])

        return ans