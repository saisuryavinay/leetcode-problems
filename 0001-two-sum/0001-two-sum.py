class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            val = nums[i]
            ans = target - val
            if ans in hash_map:
                return [hash_map[ans],i]
            hash_map[val] = i
        return [-1,-1]