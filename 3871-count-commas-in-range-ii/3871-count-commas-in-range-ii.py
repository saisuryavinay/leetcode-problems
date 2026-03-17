class Solution:
    def countCommas(self, n: int) -> int:
        tot = 0
        i = 1000
        while i <= n:
            tot+= (n-i+1)
            i*=1000
        return tot