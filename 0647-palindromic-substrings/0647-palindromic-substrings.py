class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand from center
        # odd and even
        # backtracking -> how to use
        # at each point check if we can expand
        

        # brute force
        # i to n
        # j -> i to n
        # if normal str == reversed => add 1 to res

        def expand(l, r):
            res = 0
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    return res
            return res
        
        result = 0
        for center in range(len(s)):
            for c1, c2 in [(center, center), (center, center + 1)]:
                result += expand(c1, c2)
        
        return result
