class Solution:
    def longestPalindrome(self, s: str) -> str:
        # min? 1 to 1k
        # only letters and digits
        # babad -> bab or aba
        
        # brute force -> i and j
        # if normal string == reversed string, compare it with len of best string
        # if >, update best string
        # return

        # O(n^2). 
        # O(N)
        # brute force
        # best = ""
        # n = len(s)
        # for i in range(n):
        #     for j in range(i, n):
        #         substr = s[i:j+1]
        #         if substr == substr[::-1] and len(substr) > len(best):
        #             best = substr
        
        # return best

        # Optimized 2 pointer
        # treat each index as center
        # keep expanding until palindrome
        # update best accordingly

        def expand_helper(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        best = ""
        
        for ind, center in enumerate(s):
            # TODO: check oob
            for c1, c2 in [(ind, ind), (ind, ind+1)]:
                curr_best = expand_helper(c1, c2)
                if len(curr_best) > len(best):
                    best = curr_best
        
        return best