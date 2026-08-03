class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        for v in hash_map.values():
            if v > 1:
                return True
        return False