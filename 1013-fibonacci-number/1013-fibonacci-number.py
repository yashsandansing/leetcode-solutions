class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev = 0
        curr = 1
        res = 0
        for i in range(2, n + 1):
            res = prev + curr
            prev = curr
            curr = res


        return res