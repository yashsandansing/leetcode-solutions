class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # sliding window 
        # min len - min(len(s), 2)
        # max len - min(26, len(s))

        # sliding window
        # r increments over s[r]
        # [] <- 26
        # unique -> +1 increment. result = 1
        # if unique > 2: if yes, shrink windoe
        # shrink window decrement by 1
        # if ele[idx] == 0: unique -= 1

        uniq = 0
        l = 0
        counts = defaultdict(int)
        res = 0
        for r in range(len(s)):
            char = s[r]
            counts[char] += 1

            if counts[char] == 1:
                uniq += 1
            
            while uniq > 2:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    uniq -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res