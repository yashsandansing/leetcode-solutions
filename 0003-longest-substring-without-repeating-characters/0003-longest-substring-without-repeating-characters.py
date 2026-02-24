class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # len -> 0 to 10^4
        # letters digits symbols spaces
        
        # brute force -> i, j
        # initialize a dict => enter current val and max_freq. if max_freq > 1. break out of j
        # return best_len

        # abcdb

        best = 0
        n = len(s)
        l = r = 0
        last_occurence = dict()
        while r < n:
            
            char = s[r]
            
            if char in last_occurence:
                l = max(l, last_occurence[char] + 1)
            last_occurence[char] = r
            best = max(best, r - l + 1)
            r += 1

        return best