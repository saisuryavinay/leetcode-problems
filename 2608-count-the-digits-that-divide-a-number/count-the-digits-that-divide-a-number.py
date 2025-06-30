class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        original = num 
        while num > 0:
            r = num % 10
            if r != 0 and original % r == 0: 
                c += 1
            num //= 10
        return c
