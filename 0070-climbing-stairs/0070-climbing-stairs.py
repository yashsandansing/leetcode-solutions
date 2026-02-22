class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for step in range(3, n + 1):
            curr = first + second
            first = second
            second = curr

        return second