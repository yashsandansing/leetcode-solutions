class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        MIN_INT, MAX_INT = -2**31, (2**31) - 1

        res = 0

        while i<n and s[i] == " ":
            i += 1
        
        if i == n:
            return 0
        
        if s[i] == "-":
            sign = -1
            i+=1
        elif s[i] == "+":
            i+=1
        
        while i<n and '0' <= s[i] <= '9':
            res = res*10 + (ord(s[i]) - ord('0'))
            if sign == 1 and res>MAX_INT:
                return MAX_INT
            if sign == -1 and -res < MIN_INT:
                return MIN_INT
            i += 1
        return res*sign