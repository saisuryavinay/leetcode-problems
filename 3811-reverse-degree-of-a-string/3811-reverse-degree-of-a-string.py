class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ele = 26 + 97 - ord(s[i])
            ans += (i+1)*ele
        return ans