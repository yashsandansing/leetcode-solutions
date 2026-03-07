class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        while s[n] == " ":
            n -= 1
        length = 0
        while s[n] != " " and n > -1:
            length += 1
            n -= 1
        return length