class Solution:
    def countRotations(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i] == s[(i+1) % len(s)]:
                ans += 1
        if k == ans - 1:
            return ans
        if k == ans:
            return len(s) - ans
        return 0