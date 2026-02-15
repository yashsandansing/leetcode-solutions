class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(n_open, n_closed):
            if len(stack) == n * 2:
                res.append("".join(stack.copy()))
                return
            
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_closed)
                stack.pop()
            
            if n_closed < n_open:
                stack.append(")")
                backtrack(n_open, n_closed + 1)
                stack.pop()
            
            return 

        backtrack(0, 0)
        return res