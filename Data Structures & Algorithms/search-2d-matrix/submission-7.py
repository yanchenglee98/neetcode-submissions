import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect.bisect_right([r[0] for r in matrix], target) - 1
        b = bisect.bisect_left(matrix[row], target) 
        return False if b >= len(matrix[0]) else matrix[row][b]==target 
