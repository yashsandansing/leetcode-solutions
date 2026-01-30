class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # q = deque()
        # for num in arr:
        #     if len(q) < k:
        #         q.append(num)
        #     elif abs(q[0] - x) > abs(num - x):
        #         q.popleft()
        #         q.append(num)

        # return list(q)

        # using binary search
        # how to solve it?
        # set l to 0 and r to len(arr) - k
        # bcs need to return arr[l:l+k]
        # use two pointers -> mid and (mid+k)
        # at each step check if x<=arr[mid] or x>arr[mid + k]
        # if x<=arr[mid] -> set r to mid (no concern with right half to find l)
        # if x>arr[mid + k] -> set l to mid + 1, because the prev ones are irrelevant
        # if arr[mid] < x < arr[mid + k] -> check which element x is closer to and update
        # l or r accordingly
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x <= arr[m]:
                r = m
            elif x > arr[m + k]:
                l = m + 1
            else:
                diff_low = abs(arr[m] - x)
                diff_high = abs(arr[m + k] - x)

                if diff_low <= diff_high:
                    r = m
                else:
                    l = m + 1
        
        return arr[l : l + k]
