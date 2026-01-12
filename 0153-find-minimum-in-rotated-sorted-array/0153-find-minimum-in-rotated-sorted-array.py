class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 5001

        while l<=r:
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res