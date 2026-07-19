class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            elif nums[left] < target:
                left += 1
            else:
                right -=1 
        return -1