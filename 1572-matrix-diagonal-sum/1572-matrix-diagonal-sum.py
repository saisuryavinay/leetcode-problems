class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = []
        n = len(mat)
        for i in range(n):
            res.append(mat[i][i])

        for i in range(n):
            if i != n - 1 - i:   
                res.append(mat[i][n - 1 - i])
                
        return sum(res)