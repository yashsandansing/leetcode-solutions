class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1) - 1

        while True:
            m = (l + r) // 2
            n = half - m - 2

            A1 = nums1[m] if m >= 0 else float('-inf')
            B1 = nums2[n] if n >= 0 else float('-inf')

            A2 = nums1[m + 1] if m + 1 < len(nums1) else float('inf')
            B2 = nums2[n + 1] if n + 1 < len(nums2) else float('inf')

            if A1 <= B2 and B1 <= A2:
                if total % 2 == 0:
                    return (max(A1, B1) + min(A2, B2)) / 2
                
                return min(A2, B2)
            
            else:
                if A1 > B2:
                    r = m - 1
                else:
                    l = m + 1