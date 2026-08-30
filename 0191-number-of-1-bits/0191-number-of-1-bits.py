class Solution:
    def hammingWeight(self, n: int) -> int:
        res = bin(n)[2:]
        ans = res.count('1')
        return ans