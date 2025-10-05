class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        dupe = nums
        total = 0
        for x in dupe:
            total ^= x
        if total != 0:
            return len(dupe)
        if all(x == 0 for x in dupe):
            return 0
        return len(dupe) - 1
