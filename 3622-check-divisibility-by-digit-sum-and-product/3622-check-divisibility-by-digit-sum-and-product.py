class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        res = n
        num = n
        while num > 0:
            digit_sum += num % 10
            num //= 10
        digit_prod = 1
        while n > 0:
            digit_prod *= n % 10
            n //= 10
        ans = digit_sum + digit_prod
        if res % ans == 0:
            return True
        else:
            return False
