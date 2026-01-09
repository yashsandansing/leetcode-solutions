class FreqStack:

    def __init__(self):
        self.counts = {}  # map element to num occurences
        self.stack1 = []
        self.stack2 = []  # use to hold elements after the most freq is popped

    def push(self, val: int) -> None:
        self.stack1.append(val)
        self.counts[val] = self.counts.get(val, 0) + 1

    def pop(self) -> int:
        maxCount = -1
        for ele, count in self.counts.items():
            maxCount = max(maxCount, count)
        ind = 0
        for ind in range(len(self.stack1)-1, -1, -1):
            ele = self.stack1[ind]
            if self.counts[ele] == maxCount:
                break
        
        while self.stack1:
            poppedEle = self.stack1.pop()
            if poppedEle == ele:
                break
            self.stack2.append(poppedEle)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        self.counts[ele] = max(self.counts[ele]-1, 0)
        return ele

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()