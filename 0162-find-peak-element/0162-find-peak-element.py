class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # if upward slope, go up
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            # it's a downward slope ahead, go right
            else:
                r = mid
        # could return either l or r since 
        # they'll be equal in the end
        return l