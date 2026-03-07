class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        start = 0
        def backtrack(start):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            for ind in range(start, n + 1):
                curr.append(ind)
                backtrack(ind + 1)
                curr.pop()
        res = list()
        curr = list()
        backtrack(1)
        return res
