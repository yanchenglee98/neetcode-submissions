class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        l,r = 0, m-1
        half = (m+n)//2
        while True:
            mid = (l+r)//2
            x = half - mid - 2
            Aleft = nums1[mid] if mid >=0 else -float('inf')
            Aright = nums1[mid+1] if (mid + 1) < m else float('inf')
            Bleft = nums2[x] if x>=0 else -float('inf')
            Bright = nums2[x+1] if (x+1) < n else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                print(m, n)
                if (m+n) % 2:
                    return min(Aright, Bright)
                else:
                     return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
        