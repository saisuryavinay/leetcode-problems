class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for ans in nums:
            if ans in hash_map:
                hash_map[ans] +=1
            else:
                hash_map[ans] = 1
        res = []
        for k,v in hash_map.items():
            if v == 1:
                res.append(k)
        return res[0]
        