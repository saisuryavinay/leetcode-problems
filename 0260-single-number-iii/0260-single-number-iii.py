class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash_map = {}
        res = [0,0]
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        i = 0
        for k,v in hash_map.items():
            if v == 1:
                res[i] = k
                i+=1
        return res
