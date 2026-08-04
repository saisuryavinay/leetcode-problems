class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = min(nums)
        m = max(nums)
        ans = set(nums)
        res = []
        for i in range(n,m+1):
            if i not in ans:
                res.append(i)
        return res