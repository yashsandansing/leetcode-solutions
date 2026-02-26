class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        res = 1
        for idx in range(1, len(intervals)):
            curr = intervals[idx]
            if heap[0] > curr[0]:
                heapq.heappush(heap, curr[1])
                res += 1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, curr[1])
        
        return res