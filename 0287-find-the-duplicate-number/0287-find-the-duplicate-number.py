class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            res = []
            hash_map = {}
            for num in nums:
                if num in hash_map:
                    hash_map[num]+=1
                else:
                    hash_map[num]=1
            for k,v in hash_map.items():
                if v >1:
                    res.append(k)
            return res[0]