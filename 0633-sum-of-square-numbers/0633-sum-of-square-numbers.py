import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            ans = left * left + right * right
            if ans == c:
                return True
            elif ans < c:
                left += 1
            else:
                right -= 1
        return False