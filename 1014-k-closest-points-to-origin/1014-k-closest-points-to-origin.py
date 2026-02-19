class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def helper(x, y):
            squared_distance = (x)**2 + (y)**2
            return squared_distance**0.5
        
        heap = []
        heapq.heapify(heap)

        for ind, (x, y) in enumerate(points):
            curr_dist = x**2 + y**2
            heapq.heappush(heap, (-curr_dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for d,x,y in heap]
