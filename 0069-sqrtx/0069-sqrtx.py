class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x//2
        res = -1

        while l<=r:
            m = (l + r) // 2
            m_sq = m * m
            if m_sq <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res