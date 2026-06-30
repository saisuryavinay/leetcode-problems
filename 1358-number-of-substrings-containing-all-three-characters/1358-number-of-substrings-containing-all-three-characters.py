class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash_map = {}
        l = 0
        res = 0

        for ans in range(len(s)):
            hash_map[s[ans]] = hash_map.get(s[ans], 0) + 1

            while ('a' in hash_map and hash_map['a'] > 0 and 'b' in hash_map and hash_map['b'] > 0 and 'c' in hash_map and hash_map['c'] > 0):
                res += len(s) - ans
                hash_map[s[l]] -= 1
                l += 1
                
        return res