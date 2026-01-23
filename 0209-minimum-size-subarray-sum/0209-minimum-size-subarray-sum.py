class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        l, r = 0, 0
        curr_sum = 0
        best = float('inf')

        while r < len(nums):

            if curr_sum < target:
                curr_sum += nums[r]

            while l <= r and curr_sum >= target:
                best = min(best, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1
        
        return best