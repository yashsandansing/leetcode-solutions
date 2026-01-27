# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # logic -> 3 logn solution
        # 1. find peak
        # 2. find element in first half of the array -> if found return
        # 3. find element in second half of the array -> if found return
        # 4. otherwise, return -1
        peak = [-1, -1]  # store in format: height, index
        l = 0
        r = mountainArr.length() - 1

        while l<=r:
            mid = (l + r)//2

            curr = mountainArr.get(mid)
            low = mountainArr.get(l)
            high = mountainArr.get(r)
            
            if curr >= peak[0]:
                peak = [curr, mid]

            # for each comparison,
            # add a check for checking if slope if up or down
            # and adjust l or r accordingly
            # i.e. if currNext > curr, that means slope is uphill
            # and the peak is in the right direction
            if curr > high:
                currNext = mountainArr.get(mid + 1)
                # if peak in left direction, search there
                if curr > currNext:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                currNext = mountainArr.get(mid + 1)
                if curr > currNext:
                    r = mid - 1
                else:
                    l = mid + 1

        l = 0
        r = peak[1]

        while l<=r:
            mid = (l + r) // 2

            curr = mountainArr.get(mid)
            if curr == target:
                return mid
            
            if target > curr:
                l = mid + 1
            else:
                r = mid - 1
        
        l = peak[1]
        r = mountainArr.length() - 1


        while l<=r:
            mid = (l + r) // 2

            curr = mountainArr.get(mid)
            if curr == target:
                return mid
            
            if target < curr:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1


            