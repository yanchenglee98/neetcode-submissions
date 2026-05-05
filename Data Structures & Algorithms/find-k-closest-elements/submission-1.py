class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        n = len(arr)
        for r in range(n):
            if r-l+1>k:
                if abs(arr[r]-x) < abs(arr[l]-x):
                    l+=1
        return arr[l:l+k]