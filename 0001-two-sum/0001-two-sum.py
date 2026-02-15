class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # duplicates
        # sorted
        # size of array
        # valid solution
        # negative values?

        ele_to_ind = dict()
        for ind, num in enumerate(nums):
            pred = target - num
            if pred in ele_to_ind:
                return [ind, ele_to_ind[pred]]
            ele_to_ind[num] = ind
