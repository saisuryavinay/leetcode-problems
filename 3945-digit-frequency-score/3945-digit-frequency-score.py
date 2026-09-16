class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = str(n)
        hash_map = {}
        for i in ans:
            hash_map[i] = hash_map.get(i,0) + 1
        res = 0
        for k,v in hash_map.items():
            res += int(k)*v
        return res