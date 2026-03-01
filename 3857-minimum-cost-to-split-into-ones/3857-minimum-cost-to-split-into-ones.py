class Solution:
    def minCost(self, n: int) -> int:
        ans = n * (n-1) // 2
        # print(ans)
        return ans