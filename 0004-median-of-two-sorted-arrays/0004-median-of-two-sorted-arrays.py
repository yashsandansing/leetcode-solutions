class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2 # works for both even-odd arrays
        # in case of odd arrays, 2nd half has +1 element
        A, B = nums1, nums2
        # want A to be smaller
        if len(B) < len(A):
            A, B = B, A

        l = 0
        r = len(A) - 1

        # do a binary search on A and B to find median
        while True:
            midA = (l + r) // 2
            
            # midA + 1 -> convert from index to count
            # subtract from half -> taking only required elements from 2nd array
            # final -1 -> converting from count to index
            midB = half - (midA + 1) - 1

            # take values around boundaries
            # -inf and inf is taken for ease and to say that this half
            # doesnt have enough/any elements. select inf (or *-1)
            left_A  = A[midA] if midA >= 0 else float('-inf')  # take right-most minimum value in A
            right_A = A[midA+1] if midA + 1 < len(A) else float('inf')  # take left-most maximum value in A
            left_B  = B[midB] if midB >= 0 else float('-inf')
            right_B = B[midB+1] if midB + 1 < len(B) else float('inf')

            # check if median condition is satisfied
            # since individual arrays are sorted, we check for A and B
            if left_A <= right_B and left_B <= right_A:    
                # if even we will take sum of two medians
                if total % 2 == 0:
                    return (max(left_A, left_B) + min(right_A, right_B))/2
                # if odd we want just one element
                return min(right_B, right_A)
            # if took too much from A, reduce how much you took
            elif left_A > right_B:
                r -= 1
            
            # didnt take enough elements from A
            else:
                l += 1