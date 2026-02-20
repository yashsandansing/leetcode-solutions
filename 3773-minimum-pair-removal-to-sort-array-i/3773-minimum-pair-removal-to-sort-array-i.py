class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) - 1

        while True:
            reverse = True
            # check if array has been sorted in reverse already
            for ind in range(n):
                if nums[ind + 1] < nums[ind]:
                    reverse = False
                    break
            
            if reverse == True:
                return res
            # one deletion + replacement required
            res += 1
            min_idx, min_sum = -1, float('inf')

            # loop to track the least sum
            for ind in range(n):
                curr_sum = nums[ind] + nums[ind + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_idx = ind
            # update the first index of the two elements 
            # with the least sum
            nums[min_idx] = min_sum

            # for all following elements
            # update current with the next value
            # (since we replaced the value with the sum)
            # the 2nd num is not needed anymore
            for idx in range(min_idx + 1, n):
                nums[idx] = nums[idx + 1]

            # since we removed one value,
            # reduce n by 1 to shrink our window          
            n -= 1
        
        # should never reach here
        return -1