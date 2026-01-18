class Solution:
    def trap(self, height: List[int]) -> int:

        trapped = 0
        l, r = 0, len(height) - 1
        max_l = max_r = 0

        while l<r:
            if height[r] > height[l]:
                max_l = max(max_l, height[l])
                trapped += max_l - height[l]
                l += 1
            else:
                max_r = max(max_r, height[r])
                trapped += max_r - height[r]
                r -= 1
        
        return trapped

            
            
        