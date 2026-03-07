class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n

        for ind in range(n - 1, -1, -1):
            if ind + nums[ind] >= goal:
                goal = ind
        
        return goal == 0