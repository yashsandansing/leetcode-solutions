class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # len -> 1 to 10^4
        # can start == end? yes
        
        # sorted? -> no
        # (1, 4), (4, 7) => (1, 7)

        # thoughts
        # sort it by their start times (secondary is end)
        # for a pair check if they are intersecting
        # end[0] >= start[1] => yes
        # merge them => [min(start), max(end)]
        # stack = [] => [(1, 5)]

        # guessing that it sorts by i[0] and i[1]
        intervals.sort()
        stack = [intervals[0]]

        for idx in range(1, len(intervals)):
            curr_start, curr_end = intervals[idx]
            prev_start, prev_end = stack[-1]

            if prev_end >= curr_start:
                stack[-1][1] = max(prev_end, curr_end)
            else:
                stack.append([curr_start, curr_end])

        return stack
