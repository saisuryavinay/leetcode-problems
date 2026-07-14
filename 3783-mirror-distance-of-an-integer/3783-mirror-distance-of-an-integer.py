class Solution:
    def mirrorDistance(self, n: int) -> int:
        ans = str(n)[::-1]
        return abs(n-int(ans))