class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        # if len(needle) == len(haystack):
        #     return 0 if needle == haystack else -1
        k = len(needle)
        n = len(haystack)
        for start in range(0, n - k + 1):
            if needle == haystack[start : start + k]:
                return start
        
        return - 1
