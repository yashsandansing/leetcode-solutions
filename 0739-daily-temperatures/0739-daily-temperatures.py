class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 to 10**5
        # positive
        # duplicates
        # monotonically decreasing stack
        # if temp > stack[-1] -> upda

        # res[stack[ind]] = curr_ind = stack[ind]
        # stack.append(ind)

        res = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = ind - prev
            stack.append(ind)

        return res