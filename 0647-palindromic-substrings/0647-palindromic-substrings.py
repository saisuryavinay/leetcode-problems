class Solution:
    def isPalindrome(self,s):
        if s == s[::-1]:
            return True
        else:
            return False

    def countSubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            for j in range(i + 1,len(s)+1):
                res.append(s[i:j])
        c = 0
        for i in range(len(res)):
            if self.isPalindrome(res[i]):
                c += 1
        return c