class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # store at least one character in the string
        # so that if s starts with a valid character
        # start calculating from -1
        stack = [-1]
        max_valid = 0

        for idx, brac in enumerate(s):
            if brac == "(":
                stack.append(idx)
            else:
                stack.pop()
                # if stack == 0, that means current character is the latest
                # invalid character (closing before opening or not matching opening)
                # append current idx to stack since it would be the only character in
                # the stack. if an opening is added, it would be popped by another closing
                # if another closing is added, this one would be popped and replaced instead
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    max_valid = max(max_valid, idx - stack[-1])

        return max_valid