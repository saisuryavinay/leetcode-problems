class Solution:
    def isPalindromic(self, s: str) -> bool:
        res = []
        for c in s:
            res.append(ord(c))
        ans = ""
        for i in range(len(res)):
            ans += bin(res[i])[2:].zfill(8)
        return ans == ans[::-1]