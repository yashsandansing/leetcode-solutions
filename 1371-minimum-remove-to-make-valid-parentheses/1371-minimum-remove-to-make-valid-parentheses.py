class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        # use stack to maintain brackets
        stack = []
        for ind, char in enumerate(s):
            # if open bracket -> add to stack
            if char == "(":
                stack.append(ind)
            # if closed bracket encountered, pop from stack
            # if nothing to pop -> set current value to empty (invalid bracket)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[ind] = ""
        # after iterating over entire string, 
        # if stack not empty (open bracket invalid -> not found it's closing)
        # invalidate open bracket's indices by setting to ""
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)
