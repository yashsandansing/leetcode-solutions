class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # interval comes before newInterval

        # 1. newInterval -> before interval
        # 2. newInterval -> after 'x' intervals
        # 3. newInterval -> merges some intervals

        # go through all intervals that have an end time > newIntervalTime
        # end_time <= newIntervalTime: break -> ind
        # go through the rest and carefully merge intervals in newInterval till index runs out/interval[0]>newInterval[1]

        result = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            elif interval[1] < newInterval[0]:
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        return result