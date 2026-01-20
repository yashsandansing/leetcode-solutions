class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(ind, curr):
            if ind == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[ind])
            dfs(ind+1, curr)
            curr.pop()
            dfs(ind+1, curr)
            return
        
        dfs(0, [])
        return res