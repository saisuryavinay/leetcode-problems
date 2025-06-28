class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            ans = 0
            while n > 0:
                digit = n % 10
                ans += digit * digit
                n = n // 10
            if ans == 1:
                return True
            elif ans == 4:
                return False  
            n = ans
