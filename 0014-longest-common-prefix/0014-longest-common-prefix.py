class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for idx in range(1, len(strs)):
            n = len(prefix)
            while n > 0 and prefix[:n] != strs[idx][:n]:
                n -= 1
            prefix = prefix[:n]
        
        return prefix
            