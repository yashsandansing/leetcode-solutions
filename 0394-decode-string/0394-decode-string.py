class Solution:
    def decodeString(self, s: str) -> str:
        # use a default 1 count to multiply strings with
        # use ] to decide when to add something/ multiply with num
        # use [ to decide when to possibly join something (chain)
        
        # stack = []
        # nums = [] 
        # num = 2
        # res = ""

        stackLetters = [] # use to hold stack of letter after [ is encountered
        stackCounts = [] # use to hold counts when [ is encountered to calculate nested loops
        num = 0
        res = ""
        curr = ""

        for c in s:
            if c.isdigit():
                num = num*10 + int(c)

            elif c == "[":
                # print("[", curr, num)
                stackCounts.append(num)
                stackLetters.append(curr)
                
                num = 0
                curr = ""

            elif c == "]":
                temp = curr
                curr = stackLetters.pop()
                count= stackCounts.pop()
                curr+=temp*count
            else:
                curr+=c
        
        return curr