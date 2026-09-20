class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        sorted_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
        # print(sorted_map)
        res = []
        for key,v in sorted_map.items():
            if k != 0:
                res.append(key)
                k -= 1
        return res