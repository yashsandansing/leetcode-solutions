class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # [-3, 3] max heap for min eles
        # [5, 6] min heap for max eles

        # append 1, -1, -1, 3
        # check if nums[l] is at the top, if yes -> evict
        # to be evicted -> -3
        invalid_map = defaultdict(int)
        small_heap = list()
        large_heap = list()

        for i in range(k):
            heapq.heappush(small_heap, -1 * nums[i])
        for i in range(k//2):
            # rebalance (in case k is large (50k))
            val = -1 * heapq.heappop(small_heap)
            heapq.heappush(large_heap, val)

        res = list()
        if k % 2 == 1:
            res.append(-1 * small_heap[0])
        else:
            res.append((-1 * small_heap[0] + large_heap[0]) / 2)
        valid = 0
        invalid_vals = defaultdict(int)
        for i in range(k, len(nums)):

            in_num = nums[i]
            out_num = nums[i - k]
            balance = 0

            if out_num <= -1 * small_heap[0]:
                balance -= 1
            else:
                balance += 1
            invalid_vals[out_num] += 1

            if small_heap and in_num <= small_heap[0] * -1:
                heapq.heappush(small_heap, in_num * -1)
                balance += 1
            else:
                heapq.heappush(large_heap, in_num)
                balance -= 1
            
            if balance < 0:
                val = heapq.heappop(large_heap)
                heapq.heappush(small_heap, -1 * val)
                balance += 1
            elif balance > 0:
                val = -1 * heapq.heappop(small_heap)
                heapq.heappush(large_heap, val)
                balance -= 1
            
            while invalid_vals[-1 * small_heap[0]] > 0:
                ele = -1 * heapq.heappop(small_heap)
                invalid_vals[ele] -= 1
            
            while large_heap and invalid_vals[large_heap[0]] > 0:
                ele = heapq.heappop(large_heap)
                invalid_vals[ele] -= 1

            if k % 2 == 1:
                res.append(-1 * small_heap[0])
            else:
                res.append((-1 * small_heap[0] + large_heap[0]) / 2)
        
        return res