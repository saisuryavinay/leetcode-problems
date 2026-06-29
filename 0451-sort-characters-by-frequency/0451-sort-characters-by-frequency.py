class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        res = ""
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        Updated_hash_map = dict(sorted(hash_map.items(),reverse = True, key = lambda x: x[1]))
        for k,v in Updated_hash_map.items():
            res += (k*v)
        return res