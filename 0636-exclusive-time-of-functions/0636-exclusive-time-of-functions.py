class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        prev = 0

        for log in logs:
            process, type, time = log.split(":")
            process, time = int(process), int(time)

            if type == "start":
                if stack:
                    prev_process = stack[-1]
                    res[prev_process] += time - prev

                stack.append(process)
                prev = time

            else:
                curr = stack.pop()
                res[curr] += time - prev + 1
                prev = time + 1
        
        return res