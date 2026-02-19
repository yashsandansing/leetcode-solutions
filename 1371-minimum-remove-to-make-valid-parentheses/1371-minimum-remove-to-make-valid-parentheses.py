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

        extra_opens = total_opens = 0
        temp = ""
        # loop 1 for alpha and closes
        for char in s:
            if char == '(':
                total_opens += 1
                extra_opens += 1
                temp += char

            elif char == ')':
                if extra_opens == 0:
                    continue
                extra_opens -= 1
                temp += char

            else:
                temp += char
        
        if extra_opens == 0: return temp
        
        res = ""
        # loop 2 for extra_opens
        keep = total_opens - extra_opens

        for char in temp:
            if char == "(":
                if keep > 0:
                    res += char
                    keep -= 1
            else:
                res += char

        return res