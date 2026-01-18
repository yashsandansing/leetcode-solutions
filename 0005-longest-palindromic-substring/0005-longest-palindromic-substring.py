class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for c in range(len(s)):
            # for odd checks
            i = j = c
            while i>0 and j<len(s)-1 and s[i-1] == s[j+1]:
                # print(i, j)
                i -= 1
                j += 1
            if j - i > end - start:
                start, end = i, j
            
            i, j = c, c+1
            if j<len(s) and s[i] == s[j]:
                while i>0 and j<len(s)-1 and s[i-1] == s[j+1]:
                    i -= 1
                    j += 1
                
                if j - i > end - start:
                    start, end = i, j
        
        return s[start: end+1]