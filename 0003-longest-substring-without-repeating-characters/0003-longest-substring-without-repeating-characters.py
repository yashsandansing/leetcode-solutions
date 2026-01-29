class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        last_index = {}  # store last occurence
        l = 0
        res = 0
        for r in range(len(s)):
            
            # check if element in current list
            if s[r] in last_index:
                # update l directly instead of incrementing by 1
                # max operation to avoid going back
                l = max(last_index[s[r]] + 1, l)
            last_index[s[r]] = r

            res = max(res, r - l + 1)
        
        return res