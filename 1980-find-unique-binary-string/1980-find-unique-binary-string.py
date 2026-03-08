class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        res1 = []
        for num in nums:
            res.append(int(num, 2))
        n = len(nums)
        for i in range(0, 2**n):
            res1.append(bin(i)[2:].zfill(n))
        for ans in res1:
            if ans not in nums:
                return ans