class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastCount = dict() # element: last_index

        for ind, num in enumerate(nums):
            if lastCount.get(num) is not None and abs(lastCount[num] - ind) <= k:
                return True
            lastCount[num] = ind

        return False