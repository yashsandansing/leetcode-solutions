class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ind = abs(num) - 1
            if nums[ind] < 0:
                return abs(num)
            nums[ind] *= -1
        