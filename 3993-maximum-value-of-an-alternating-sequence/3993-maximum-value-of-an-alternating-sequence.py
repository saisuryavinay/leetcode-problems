class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s

        ans = n // 2
        return s + m + (ans - 1) * (m - 1)