class Solution:
    def reverse(self, x: int) -> int:
        # 0 to trillion
        # negative values
        
        
        # num = 0
        # x % 10 => 1
        # num = num*10 + x => 321
        # x = x // 10 => 0
        num = 0
        sign = 1
        MAX_INT = (2**31) - 1
        
        if x < 0:
            sign = -1
            x = -x

        while x > 0:
            num = num * 10 + (x % 10)
            x = x // 10
        
        if num > MAX_INT:
            return 0
        return sign*num
