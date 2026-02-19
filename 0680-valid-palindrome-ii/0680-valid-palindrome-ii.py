class Solution:
    def validPalindrome(self, s: str) -> bool:
        # empty? -> no
        # lowercase only? -> yes
        
        # len -> large number
        
        # 2 approaches -> center, 2 pointers at each end
        # 2 pointers -> l = 0 and r = end


        # helper for when substrings dont match
        def helper(l, r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l<=r:
            if s[l] != s[r]:
                # use skip logic to skip left by 1 and right by 1
                # return immediately cus its true or false
                skip = helper(l+1, r) or helper(l, r-1)
                return skip
            # normal string/palindrome
            else:
                l += 1
                r -= 1
        # return True when no deletions needed
        return True
            