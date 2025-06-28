class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        p = x
        sum=0
        while x >0:
            r = x%10
            sum+=r
            x = x//10
        if(p%sum==0):
            return sum
        return -1