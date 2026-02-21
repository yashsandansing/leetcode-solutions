class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1, 2, 3]
        # hashmap -> stores curr_sum: count (how many times this sum has been encountered)
        # at each step, do curr_sum - k. if this exists in the hashmap
        # add to res => there are these many ways to remove (curr_sum - k) to get to curr result
        # i.e. k

        prefix_sum = {0 : 1}
        res = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefix_sum.get(diff, 0)

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return res