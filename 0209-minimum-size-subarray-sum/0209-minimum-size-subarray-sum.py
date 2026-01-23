class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0
        
        l, r = 0, 0
        curr_sum = 0
        best = float('inf')
        
        # sliding window approach
        while r < len(nums):
            
            # add r if current window allows
            if curr_sum < target:
                curr_sum += nums[r]

            # remove l if exceeded limit (imp to keep l<=r for single elements)
            while l <= r and curr_sum >= target:
                # store best before reducing
                best = min(best, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1
        
        return best