class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        map = dict(sorted(hash_map.items(), key = lambda x : x[1], reverse = True))
        ans = []
        for key,val in map.items():
            if k != 0:
                ans.append(key)
                k -= 1
        return ans