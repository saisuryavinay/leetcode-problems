class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = []
        n = len(tasks)
        for i in range(n):
            res.append(sum(tasks[i]))
        print(res)
        return min(res)