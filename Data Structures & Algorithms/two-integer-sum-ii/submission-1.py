class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            bsearch = self.binarySearch(numbers, target-numbers[i])
            print(i, bsearch, numbers[i], target-numbers[i])
            if bsearch > 0:
                return [i+1,bsearch+1]
        return [-1,-1]
    
    def binarySearch(self, ls, v):
        l, r = 0, len(ls)-1
        while l<=r:
            mid = (l+r) // 2
            if ls[mid] == v:
                return mid
            elif ls[mid] < v:
                l = mid + 1
            else:
                r = mid - 1
        return -1
   