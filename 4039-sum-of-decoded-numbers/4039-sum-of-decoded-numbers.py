class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10 **9 + 7
        tot = 0
        for num in nums:
            width = num % 10
            d = num // 10

            ans = str(d)
            x = int(ans[:width])
            y = int(ans[width:])

            tot = (tot + pow(x,y,MOD)) % MOD
        return tot