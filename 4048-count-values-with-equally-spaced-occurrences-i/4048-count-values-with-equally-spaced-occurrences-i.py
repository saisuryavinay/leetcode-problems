class Solution:
    def countSpecialIntegers(self, nums: List[int]) -> int:
        hash_map = {}
        count = 0
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], []) + [i]

        for val in hash_map.values():
            if len(val) == 3:
                if val[1] - val[0] == val[2] - val[1]:
                    count += 1

        return count