class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(search_left: bool) -> int:
            l = 0
            r = len(nums) - 1
            # index to return if found element
            # if not found, return -1
            ind = -1

            while l<=r:
                m = (l + r) // 2

                # normal binary search if elements
                # are greater or lesser than target
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                
                # if target hit
                else:
                    # store index in ind
                    ind = m
                    # search_left => we want to find the leftmost
                    # i.e. starting element -> go left by decrementing
                    # the right boundary
                    if search_left:
                        r = m - 1
                    
                    # if not search_left, we need to search_right
                    # increment left to go right in that case
                    else:
                        l = m + 1

            return ind
        
        left = binary_search(True)
        right = binary_search(False)

        return [left, right]