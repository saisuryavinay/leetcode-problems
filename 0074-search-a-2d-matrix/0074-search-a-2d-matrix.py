class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        # printing row 

        # for row in range(len(mat)):
        #     for col in range(len(mat[0])):
        #         print(mat[row][col])
        #     print('\n')

        # printing col

        #  for row in range(len(mat[0])):
        #     for col in range(len(mat)):
        #         print(mat[col][row], end = ' ')
        #     print('\n')

        for row in mat:
            low = 0
            high = len(row) - 1

            # binary search

            while low <= high:

                mid = (low+high)//2

                if row[mid] == target:
                    return True

                elif row[mid] < target:
                    low = mid + 1
                
                else:
                    high  = mid - 1


        return False