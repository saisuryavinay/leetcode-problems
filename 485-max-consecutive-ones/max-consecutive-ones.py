class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_one = 0
        num = 0
        for n in nums:
            if n:
                num += 1
                if num > max_one:
                    max_one = num
            else:
                num = 0
        return max_one