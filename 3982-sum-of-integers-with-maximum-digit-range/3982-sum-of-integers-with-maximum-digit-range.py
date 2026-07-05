class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        hash_map = {}
        for num in nums:
            ans = str(num)
            maxi = int(max(ans))
            mini = int(min(ans))
            res = maxi - mini
            if num not in hash_map:
                hash_map[num] = [res,1]
            else:
                hash_map[num][1] += 1
            maxii = -1
        for v in hash_map.values():
            if v[0] > maxii:
                maxii = v[0]
        out = 0
        for k,v in hash_map.items():
            if v[0] == maxii:
                out += k * v[1]
        return out