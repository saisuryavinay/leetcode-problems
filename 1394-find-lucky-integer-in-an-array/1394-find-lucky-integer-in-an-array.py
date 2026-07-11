class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {}
        for num in arr:
            hash_map[num] = hash_map.get(num,0) + 1
        new_map = dict(sorted(hash_map.items(), key = lambda x : x[1], reverse = True))
        for k , v in new_map.items():
            if k == v:
                return v
        else:
            return -1