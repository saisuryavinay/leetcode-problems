class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num] = 1
        res = []
        for k , v in hash_map.items():
            res.append(v)
        for i in range(len(res)):
            if res[i] > 1:
                return True
        return False