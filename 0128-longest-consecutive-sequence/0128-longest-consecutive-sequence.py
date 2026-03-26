class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        l = r = 0
        for num in setNums:
            if num - 1 in setNums:
                continue
            temp = num
            currLongest = 0
            while num in setNums:
                currLongest += 1
                num += 1
            longest = max(longest, currLongest)
        return longest
            