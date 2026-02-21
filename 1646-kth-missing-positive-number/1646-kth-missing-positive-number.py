class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # iterate through the array
        # each time get current missing numbers 
        # if missing >= k: break
        # at index k - 1 ?? -1 -> increment k times to get res
        # lr
        # 4 5 6 | k =2
        # 2

        # missing = 3
        # r = -1
        # -1 + 3 - arr[-1]
        # -1 + (3 - 6 - 1 + 1)
        # -1 -3
        # -4
        
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            missing = arr[mid] - 1 - mid
            
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l + k

