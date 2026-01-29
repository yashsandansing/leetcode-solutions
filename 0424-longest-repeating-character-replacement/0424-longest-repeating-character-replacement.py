class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # length of substring - most common element count in window = current replacements
        # if current replacements > k, increment l by 1
        maxLen = 0
        l = 0
        freqCount = dict()
        maxFreq = 0
        for ind, r in enumerate(s):
            freqCount[r] = freqCount.get(r, 0) + 1
            maxFreq = max(maxFreq, freqCount[r])
            if (ind-l+1) - maxFreq > k:
                freqCount[s[l]]-=1
                l+=1
            maxLen = max(maxLen, ind-l+1)
        return maxLen
