class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = []
        for x in nums:
            sq.append(x * x)
        sq = sorted(sq, reverse = True)
        res = 0
        n = len(sq)
        mid = (n + 1) // 2
        for i in range(mid):
            res += sq[i]
        for i in range(mid, n):
            res -= sq[i]
        return res