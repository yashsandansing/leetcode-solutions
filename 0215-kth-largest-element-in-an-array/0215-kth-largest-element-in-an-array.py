class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort the array
        # return n - kth element
        # sort in reverse
        # k - 1 th element

        # nums != []
        # k is always valid
        # k > 0
        # can have duplicates -> dont return distinct

        import heapq
        heap = []

        heapq.heapify(heap)

        for num in nums:

            # while heap is not filled
            # keep adding elements
            if len(heap) < k:
                heapq.heappush(heap, num)
                continue
            # if kth largest element in the heap
            # is smaller than num, replace it with num
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        # return kth largest element in the array
        # and smallest element in the heap
        return heap[0]