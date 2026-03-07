class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        MAX = 2**31 - 1
        num = 0

        while x > 0:
            num = num * 10 + (x % 10)
            x = x // 10
            if num > MAX:
                return 0

        return sign * num