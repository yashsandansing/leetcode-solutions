class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # len -> at least 1, 10^5
        # nums can be negative
        # num can be duplicated
        
        # [1, 0, 1, 1] => k = 1
        #  0  1  2  3     idx
        

        # hashmap -> value: index
        # when you encounter a number, check if it exists within the hashmap
        # if it does subtract its value from the current index -> if <= k, return true
        # hashmap[ele] = index

        last_occurence = dict()

        for idx, num in enumerate(nums):
            if num in last_occurence and idx - last_occurence[num] <= k:
                return True

            last_occurence[num] = idx

        return False
