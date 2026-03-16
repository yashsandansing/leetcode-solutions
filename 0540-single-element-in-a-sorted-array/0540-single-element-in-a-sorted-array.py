class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            # if mid element is different than both neighbors
            # return value
            if (m == 0 or nums[m] != nums[m - 1]) and (m == len(nums) - 1 or nums[m] != nums[m + 1]):
                return nums[m]
            
            # if left_size is odd, value is there
            # skip over m - 1'th element if it was the same as m'th
            left_size = m - 1 if nums[m - 1] == nums[m] else m
            if left_size % 2 == 1:
                r = m - 1
            else:
                l = m + 1
