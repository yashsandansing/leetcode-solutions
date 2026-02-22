class Solution:
    def maxArea(self, height: List[int]) -> int:
        # least number of bars -> 2
        # can height be 0 => yes
        # least height => 0
        # least area => 0
        
        # best = 0
        # for i in height
        # for j in range(i, height):
        # h = min(i, j)
        # w = j - i
        # best = max(best, h*w)

        # [1,8,6,2,5,4,8,3,7]

        # [0,1,2,3,4,5,6,7,8]

        best_area = 0
        l = 0
        r = len(height) - 1

        while l<r:
            min_height = min(height[l], height[r])
            w = r - l
            best_area = max(best_area, min_height * w)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return best_area