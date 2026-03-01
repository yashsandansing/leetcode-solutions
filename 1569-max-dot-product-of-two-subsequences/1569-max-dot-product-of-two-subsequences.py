class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = dict()
        def backtrack(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            if (i, j) in memo:
                return memo[(i, j)]
            skip_i = backtrack(i + 1, j)
            skip_j = backtrack(i, j + 1)
            skip_both = nums1[i] * nums2[j] + max(0, backtrack(i + 1, j + 1))
            memo[(i, j)] = max(skip_i, skip_j, skip_both)
            return memo[(i, j)]
        return backtrack(0, 0)