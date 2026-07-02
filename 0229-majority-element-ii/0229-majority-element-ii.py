class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = n // 3
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        res = []
        for k, v in hash_map.items():
            if v > ans:
                res.append(k)
        return res