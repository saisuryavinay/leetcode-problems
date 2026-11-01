class Solution:
    def minMergedInteger(self, arr: list[int]) -> int:
        res = []
        for i in range(0, len(arr), 2):
            num = int(str(arr[i]) + str(arr[i+1]))
            res.append(num)
        return min(res)