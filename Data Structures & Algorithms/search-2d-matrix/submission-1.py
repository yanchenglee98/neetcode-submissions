class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        return self.findCol(matrix[row], target)

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
    
    def findCol(self, arr, target) -> bool:
        l,r=0, len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==target:
                return True
            elif arr[m]<target:
                l=m+1
            else:
                r=m-1
        return False
