class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for ind,ele in enumerate(nums):
            if ele==target:
                return ind
            
        return -1