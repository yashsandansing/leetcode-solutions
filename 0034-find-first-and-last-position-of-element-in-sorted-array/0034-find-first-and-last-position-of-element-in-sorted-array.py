class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # optimal solution

        def search(target):
            l = 0
            r = len(nums)

            while l < r:
                m = (l + r) // 2

                if target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            return l
        
        first = search(target)
        last = search(target + 1) - 1

        if first <= last:
            return [first, last]
        
        return [-1, -1]