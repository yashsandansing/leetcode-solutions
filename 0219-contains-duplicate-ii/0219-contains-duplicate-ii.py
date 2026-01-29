class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # solution: store a hashmap of last counts
        lastCount = dict() # element: last_index

        # for each element, check if element has occured previously
        # if it has, subtract the indices to get the result
        # if result <= k return true, else false
        for ind, num in enumerate(nums):
            
            if lastCount.get(num) is not None and abs(lastCount[num] - ind) <= k:
                return True
            lastCount[num] = ind

        return False