class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hash_map = {}
        res = []
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        new_sorted = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse = True))
        for key,v in new_sorted.items():
            if(k != 0):
                res.append(key)
                k -= 1
        return res