class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 0 -> empty -> can fill all elements from nums2
        # m can be 0 ->
        # m + n be 0? no. would be at least 1
        # vals can be -ve too

        # [1, 1, 2, 2, 3, 3]
        # [1, 2, 3]
        i = m - 1
        j = n - 1
        idx = -1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1