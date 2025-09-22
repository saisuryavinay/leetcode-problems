class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num] = 1
        print(hash_map)
        res = []
        sum1 = 0
        for k,v in hash_map.items():
            res.append(v)
        print(res)
        n = max(res)
        for i in range(len(res)):
            if n == res[i]:
                sum1+=n
        return sum1