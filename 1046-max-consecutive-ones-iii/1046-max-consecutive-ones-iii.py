class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # req.s 
        # k can be 0
        # k <= nums.length
        # nums.length 1 to large

        # best_dist, curr_dist
        # subtract k by 1
        # if k == 0, break out of the loop
        # r -> iterate through the list
        # once k<0, iterate to increase l
        # if nums[l] == 0: k += 1 <= do this till k !< 0

        l = 0
        best_dist = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            
            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
            
            best_dist = max(best_dist, r - l + 1)
        
        return best_dist
