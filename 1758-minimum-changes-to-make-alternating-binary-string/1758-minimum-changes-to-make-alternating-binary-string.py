class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res = ""
        start = 0
        for i in range(n):
            res+=str(start)
            start = 1 - start
        res1 = ""
        start = 1
        for i in range(n):
            res1+=str(start)
            start = 1 - start
        diff = 0
        diff1 = 0
        for i in range(len(res)):
            if s[i] != res[i]:
                diff+=1
            if s[i] != res1[i]:
                diff1+=1
        return (min(diff,diff1))