class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for ch in s:
            # if ch in hash_map:
            #     hash_map[ch] += 1
            # else:
            #     hash_map[ch] = 1
            hash_map[ch] = hash_map.get(ch,0) + 1
        for ch in t:
            # if ch in hash_map:
            #     hash_map[ch] -= 1
            # else:
            #     hash_map[ch] = 0
            hash_map[ch] = hash_map.get(ch,0) - 1
        for v in hash_map.values():
            if v != 0:
                return False
        return True