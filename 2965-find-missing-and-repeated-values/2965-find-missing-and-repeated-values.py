class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        for row in grid:
            for num in row:
                res.append(num)
        num1 = res
        hash_map = {}
        ans = [0] * 2
        for num in res:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        for k,v in hash_map.items():
            if v > 1:
                ans[0] = int(k)
        num1 = list(set(res))
        n = len(num1) + 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(num1)
        missing = expected_sum - actual_sum
        ans[1] = missing
        return ans