class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # empty return -> valid
        # closed should have open. open should be closed


        # 2 pass
        # extra_open - brackets
        # total_open - all open brackets
        # ( -> increment
        # ) -> dec extra_open
        # if extra_open == 0: and ) => remove this element

        # handle open brackets: 
        # keep = total - extra
        # each open -> dec keep by 1
        # if keep = 0 and open bracket => remove this from res
        # return res

        res = list(s)
        stack = []
        for ind, char in enumerate(res):
            if char == "(":
                stack.append(ind)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    res[ind] = ""
            else:
                continue

        # handle open substrings
        while stack:
            res[stack.pop()] = ""
        
        return "".join(res)
