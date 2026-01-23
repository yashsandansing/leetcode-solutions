class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = dict()
        
        # logic here is to store counts of all elements
        # and return true if window satisfies condition
        for ind, char in enumerate(s1):
            counts[char] = counts.get(char, 0) + 1

        l, r = 0, 0
        s = s2

        while r < len(s):
            
            # check if right most element is a "need"
            if counts.get(s[r]) is not None:
                counts[s[r]] -= 1
            
            # sliding window: while window > required frame
            # make it shorter
            while l < r and r - l + 1 > len(s1):
                if counts.get(s[l]) is not None:
                    counts[s[l]] += 1
                l += 1
            
            # if we got all values that we "needed"
            # in window, return true
            if max(counts.values()) == 0:
                    return True
                    
            r += 1

        return False