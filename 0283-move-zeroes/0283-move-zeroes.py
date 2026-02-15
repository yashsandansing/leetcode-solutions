class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # z_pointer = l
        # non_z_pointer = r
        z_pointer = non_z_pointer = 0
        # l points to the left-most 0 we have
        # r is used to iterate through the list

        # if r hits the end of the array -> exit
        while non_z_pointer < len(nums):
            # if l == 0 and r != 0, swap them
            # else if both are zeroes or non zeroes, iterate normally through the list
            if nums[z_pointer] == 0 and nums[non_z_pointer]!=0:
                nums[z_pointer], nums[non_z_pointer] = nums[non_z_pointer], nums[z_pointer]
            
            # if l != 0, increment it since we might've swapped
            # the elements and l now points to a non-zero element
            # we want l to point to the first zero'th index
            if nums[z_pointer]!=0:
                z_pointer += 1
            
            # increment normally
            non_z_pointer += 1