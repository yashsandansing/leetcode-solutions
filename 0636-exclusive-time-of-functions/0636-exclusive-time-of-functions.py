class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # at least one? yes
        # no same start or end for 2 diff events
        # each func has an end
        # stack = []
        # 0, 0
        # te = 4
        # [3, 4]
        # 0, 0, 5
        # 7 - 0 + 1 - 4
        # [9]
        
        time_elapsed = 0
        # stack -> element_id, start_time, elapsed_time
        stack = []
        res = [0]*n
        total_elapsed = 0

        for log in logs:
            ele, type_, time = log.split(":")
            ele = int(ele)
            time = int(time)
            if type_ == 'start':
                stack.append([ele, time, 0])
            else:
                popped_ele, start_time, elapsed = stack.pop()
                time_to_complete = time - start_time + 1 - elapsed
                res[popped_ele] += time_to_complete
                if stack:
                    stack[-1][-1] += time_to_complete + elapsed
            print(stack)
        
        return res