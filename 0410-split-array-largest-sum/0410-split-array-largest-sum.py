class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            pred_sum = (low + high) // 2

            num_arrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > pred_sum:
                    num_arrays += 1
                    curr_sum = 0
                curr_sum += num

                if num_arrays>k:
                    break
            
            if num_arrays > k:
                low = pred_sum + 1
            else:
                high = pred_sum

        return low