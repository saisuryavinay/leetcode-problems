class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort(reverse=True)

        maxi = digits[0]
        second_max = digits[1]
        return maxi * second_max