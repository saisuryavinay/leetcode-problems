class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_ans = set(nums)
        longest = 0
        for n in num_ans:
            if n - 1 not in num_ans:
                length = 1
                while n + length in num_ans:
                    length += 1
                longest = max(longest, length)
        return longest