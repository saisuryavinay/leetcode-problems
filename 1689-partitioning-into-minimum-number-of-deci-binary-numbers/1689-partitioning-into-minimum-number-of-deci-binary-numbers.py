class Solution:
    def minPartitions(self, n: str) -> int:
        res = []
        for ans in n:
            res.append(ans)
        return (max(map(int,res)))