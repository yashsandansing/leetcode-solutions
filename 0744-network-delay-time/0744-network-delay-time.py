class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for src, dest, time in times:
            graph[src].append([dest, time])
        distances = [float('inf')] * (n + 1)
        distances[0] = 0
        distances[k] = 0
        
        heap = [[0, k]]
        heapq.heapify(heap)

        while len(heap) > 0:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > distances[node]:
                continue
            for nei, dist in graph[node]:
                total_dist = curr_dist + dist
                if total_dist < distances[nei]:
                    distances[nei] = total_dist
                    heapq.heappush(heap, [total_dist, nei])
        
        max_time = -1
        for dist in distances:
            if dist == float('inf'):
                return -1
            max_time = max(max_time, dist)

        return max_time
            
