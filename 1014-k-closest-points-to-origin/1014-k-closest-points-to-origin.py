class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap
        # points.len == 1 => k != 2
        # len => 1 to 10^4
        # order doesnt matter
        
        # go through the list
        # calc dist to origin and push it to max_heap if curr_dist < heap[0]
        # heap => (dist, ind)
        # iterate through the heap => pop and append to res

        heap = []
        heapq.heapify(heap)
        # -10, -8

        for idx, (x, y) in enumerate(points):
            curr_dist = -1 * (x**2 + y**2)
            
            if len(heap) < k:
                heapq.heappush(heap, [curr_dist, x, y])
            
            elif heap[0][0] < curr_dist:
                heapq.heappushpop(heap, [curr_dist, x, y])
        
        return [[x, y] for idx, x, y in heap]
