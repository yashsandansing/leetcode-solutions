class Solution:
    def longestPalindrome(self, s: str) -> str:
        # edge case -> empty or 1 len string
        if len(s) <= 1:
            return s

        def expand(l, r):
            # loop to check if current elements are same
            # if they are expand and check next outer elements
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            # return l+1 since thats our starting point
            # return r to stop
            # why not return r-1 too -> could be less than l+1 (in even cases like 'cb')
            # also we anyways add +1 when calculating and updating string
            return l+1, r

        res = ""

        for ind in range(len(s) - 1):

            # for odd
            l, r = expand(ind, ind)
            if r-l > len(res):
                res = s[l:r]

            # even-len palindromes

            # ind + 1 does not throw an IndexError
            # due to the checks implemented in the expand function
            l, r = expand(ind, ind + 1)
            if r-l > len(res):
                res = s[l:r]
        
        return res