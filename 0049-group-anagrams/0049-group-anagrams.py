class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for num in strs:
            ans = "".join(sorted(num))
            if ans in hash_map:
                hash_map[ans].append(num)
            else:
                hash_map[ans] = [num]
        return (list((hash_map.values())))