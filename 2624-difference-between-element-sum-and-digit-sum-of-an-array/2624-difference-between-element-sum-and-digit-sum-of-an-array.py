
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_ele = 0
        digi = []
        for num in nums:
            sum_ele += num
        print(sum_ele)
        for num in nums:
            if num < 10:
                digi.append(num)
            else:
                while num > 0:
                    r = num % 10
                    digi.append(r)
                    num //= 10
        print(digi)
        digi_ele = sum(digi)
        return abs(sum_ele - digi_ele)
