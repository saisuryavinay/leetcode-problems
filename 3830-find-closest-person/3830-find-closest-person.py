class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        count  = abs(x-z)
        count1 = abs(y-z)
        if count< count1:
            return 1
        elif count1 < count:
            return 2
        return 0