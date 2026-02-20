class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) - 1

        while True:
            reverse = True
            for ind in range(n):
                if nums[ind + 1] < nums[ind]:
                    reverse = False
                    break
            
            if reverse == True:
                return res
            
            res += 1
            min_idx, min_sum = -1, float('inf')

            for ind in range(n):
                curr_sum = nums[ind] + nums[ind + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_idx = ind
            
            nums[min_idx] = min_sum
            for idx in range(min_idx + 1, n):
                nums[idx] = nums[idx + 1]
            
            n -= 1
        
        return -1