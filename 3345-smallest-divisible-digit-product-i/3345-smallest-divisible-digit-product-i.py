class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def helper(num):
            prod = 1

            while num:
                prod *= num % 10
                num = num // 10
            return prod

        while helper(n) % t != 0:
            n += 1
        return n