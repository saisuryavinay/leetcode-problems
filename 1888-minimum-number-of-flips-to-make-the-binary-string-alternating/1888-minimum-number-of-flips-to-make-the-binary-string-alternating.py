class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        res = ""
        start = 0
        for i in range(len(s)):
            res += str(start)
            start = 1 - start
        res1 = ""
        start = 1
        for i in range(len(s)):
            res1 += str(start)
            start = 1 - start
        diff = 0
        diff1 = 0
        l = 0
        ans = float('inf')

        for r in range(len(s)):
            if s[r] != res[r]:
                diff += 1
            if s[r] != res1[r]:
                diff1 += 1

            if r - l + 1 > n:
                if s[l] != res[l]:
                    diff -= 1
                if s[l] != res1[l]:
                    diff1 -= 1
                l += 1

            if r - l + 1 == n:
                ans = min(ans, diff, diff1)

        return ans