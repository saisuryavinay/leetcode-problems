class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        data = list(set(nums))       
        data.sort(reverse=True)
        res = data[:k] 
        return res