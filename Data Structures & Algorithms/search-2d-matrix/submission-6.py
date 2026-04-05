import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect.bisect_right([r[0] for r in matrix], target) - 1
        print(row)
        b = bisect.bisect_left(matrix[row], target) 
        return False if b >= len(matrix[0]) else matrix[row][b]==target 

    def findRow(self, matrix, target):
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                return m
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        return -1
