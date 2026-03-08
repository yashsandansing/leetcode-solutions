class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        self.prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        left = self.prefix_sum[left - 1] if left > 0 else 0
        return self.prefix_sum[right] - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)