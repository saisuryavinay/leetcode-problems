class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        ans = nums[n//2]
        return hash_map[ans] == 1