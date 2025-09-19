class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 0
        for i in range(1,n+1):
            ans = first+second
            second = first
            first = ans
        return ans