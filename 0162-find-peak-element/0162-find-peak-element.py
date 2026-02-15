class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # base peak -> first element
        # [0, 1, ..., n-2, n-1]
        # log n -> binary search
        # [0, 1, 2, 1, 5, 7, 6]
        peak = nums[0]
        n = len(nums)
        for ind in range(n - 1):
            if nums[ind] > nums[ind + 1]:
                return ind
            peak = nums[ind]
        return n - 1
