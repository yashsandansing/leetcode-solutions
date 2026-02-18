class Solution:
    def trap(self, height: List[int]) -> int:
        # num -> 1 to large number
        # ret -> 0 to inf.
        
        # 2 pointers. l and r
        # point to start and end
        # move l when l<=r
        # move r otherwise
        # collect water by calculating the difference
        # after collecting update heights and compare

        l = 0
        r = len(height) - 1
        total = 0
        max_l = max_r = 0

        while l<r:
            if height[l] <= height[r]:
                max_l = max(max_l, height[l])
                total += max_l - height[l]
                l += 1
            else:
                max_r = max(max_r, height[r])
                total += max_r - height[r]
                r -= 1
        
        return total