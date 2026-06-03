class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        for col in zip(*mat):
            res.append(list(col)[::-1])
        for i in range(len(res)):
            mat[i] = res[i]