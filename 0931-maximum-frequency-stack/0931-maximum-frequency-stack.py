class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)  # freq -> [list of ele]
        self.counts = defaultdict(int)  # ele -> freq
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.counts[val]+=1
        self.freq[self.counts[val]].append(val)
        self.maxCount = max(self.maxCount, self.counts[val])

    def pop(self) -> int:
        popped_ele = self.freq[self.maxCount].pop()
        self.counts[popped_ele] = max(self.counts[popped_ele]-1, 0)
        if len(self.freq[self.maxCount]) == 0:
            self.maxCount-=1
        return popped_ele


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()