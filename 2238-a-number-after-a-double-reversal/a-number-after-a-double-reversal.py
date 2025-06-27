class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #return num == 0 or num%10 !=0
        actual_num = num
        rev1 = 0
        while num>0:
            r = num%10
            rev1 = rev1*10+r
            num //=10
        new = rev1
        rev2 = 0
        while new>0:
            r1 = new%10
            rev2 = rev2*10+r1
            new//=10
        if rev2 == actual_num:
            return True
        return False