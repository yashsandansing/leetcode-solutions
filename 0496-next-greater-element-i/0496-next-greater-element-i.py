class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute-force
        # for i in nums1
        # check for subsequent array in nums2
        # after finding idx, iterate till a greater element is found
        # else: just update

        # can use stack with hashmap
        # hashmap -> element: next_highest_ele
        # use monotonically decreasing stack
        # if following ele > stack[-1] => keep popping from stack
        # and add element to hashmap
        
        hashmap = dict()  # val: next_highest_val
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                ele = stack.pop()
                hashmap[ele] = num
            
            stack.append(num)
        
        for ele in stack:
            hashmap[ele] = -1
        
        for ind, num in enumerate(nums1):
            nums1[ind] = hashmap[num]
        
        return nums1
        