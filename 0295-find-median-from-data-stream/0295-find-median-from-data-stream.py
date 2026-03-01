class MedianFinder:

    def __init__(self):
        # [1, ], # [2, 3]
        self.lower = list() # max heap for storing lower half/min elements
        self.higher = list() # min heap for storing upper half/max elements

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -1 * num)
        
        if (self.higher and self.lower) and -1 * self.lower[0] > self.higher[0]:
            self.rebalance(self.lower, self.higher)
        
        if len(self.lower) > len(self.higher) + 1:
            self.rebalance(self.lower, self.higher)
        
        if len(self.higher) > len(self.lower) + 1:
            self.rebalance(self.higher, self.lower)
        
    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -1 * self.lower[0]
        if len(self.lower) < len(self.higher):
            return self.higher[0]
        
        return (-1 * self.lower[0] + self.higher[0]) / 2
    
    def rebalance(self, host: list, receiver: list) -> None:
        num = -1 * heapq.heappop(host)
        heapq.heappush(receiver, num)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()