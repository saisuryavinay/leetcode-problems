class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        res = []
        current_sum = 0
        for i in range(1, n + 1):
            if is_prime(i):
                if current_sum + i <= s:
                    res.append(i)
                    current_sum += i
                else:
                    break
        return res