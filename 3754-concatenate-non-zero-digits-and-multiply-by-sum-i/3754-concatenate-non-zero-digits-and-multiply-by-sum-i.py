class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = str(n)
        sumi = 0
        for digit in res:
            sumi += int(digit)
        num = 0
        for digit in res:
            if digit != '0':
                num = num * 10 + int(digit)
        return num * sumi 