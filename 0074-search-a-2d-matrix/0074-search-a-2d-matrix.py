class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = low + (high - low) // 2
            midval = mat[mid // n][mid % n]
            if midval == target:
                return True
            elif midval > target:
                high = mid - 1
            else:
                low = mid + 1
        return False