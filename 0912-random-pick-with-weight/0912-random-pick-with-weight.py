class Solution:

    def __init__(self, w: List[int]):
        self.w = [i/sum(w) for i in w]
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        seed = random.uniform(0, 1)
        for i, n in enumerate(self.w):
            if seed <= n:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()