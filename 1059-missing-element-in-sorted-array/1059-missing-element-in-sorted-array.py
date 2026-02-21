class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            missing = nums[m] - nums[0] - m

            if missing < k:
                l = m + 1
            else:
                r = m - 1
        
        return nums[r] + (k - (nums[r] - nums[0] - r))
