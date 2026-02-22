class Solution:
    def climbStairs(self, n: int) -> int:
        [1, 2, 3, 4, 5, 6, 7]
       
        steps = [1, 1]
        step = 2
        for s in range(step, n + 1):
            steps.append(steps[-1] + steps[-2])

        return steps[n]