class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (smallest_ind, h)
        maxArea = 0

        for ind, h in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > h:
                smallest_ind, height = stack.pop()
                currArea = height * (ind - smallest_ind)
                maxArea = max(maxArea, currArea)
                start = smallest_ind
            
            stack.append((start, h))
        
        for (i, h) in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        
        return maxArea
