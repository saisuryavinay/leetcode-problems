class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_map = {}
        res = []
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        for k, v in hash_map.items():
            if v == 2:
                res.append(k)
        n = len(nums)
        for i in range(1, n+1):
            if i not in hash_map:
                res.append(i)
        return res