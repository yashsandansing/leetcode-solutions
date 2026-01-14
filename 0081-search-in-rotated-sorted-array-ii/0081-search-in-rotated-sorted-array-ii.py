class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid] and nums[r] == nums[mid]:
                l += 1
                r -= 1
                continue
            
            # check if 2nd half is sorted
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # check 1st half
            elif nums[mid] > nums[r]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                r -= 1
        return False
                