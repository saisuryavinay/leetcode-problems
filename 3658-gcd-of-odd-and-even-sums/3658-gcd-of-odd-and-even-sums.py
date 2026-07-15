import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        sumOdd += (n*n)
        sumEven += n * (n + 1)
        return math.gcd(sumOdd,sumEven)