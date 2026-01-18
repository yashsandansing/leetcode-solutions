class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        res = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (j-i+1 > maxLen) and self.isPalindrome(s, i, j):
                    res = s[i:j+1]
                    maxLen = j - i + 1
        
        return res


    def isPalindrome(self, s:str, i: int, j: int) -> bool:
        # print('palindrome check for', i, j)
        while i<=j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True