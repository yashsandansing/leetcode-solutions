class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_valid = 0

        for idx, brac in enumerate(s):
            if brac == "(":
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    max_valid = max(max_valid, idx - stack[-1])

        return max_valid