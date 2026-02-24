class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # at least one building
        # heights can be from 1 to really large
        # return list should be ordered -> from left to right

        # brute-force
        # l to right
        # i to i + 1
        # if any j exists that is greater than i, dont add i to list
        # if we are at end of the list and we havent encountered
        # any height add i to the list

        res = []
        n = len(heights)
        # if stack is empty or curr height < stack[-1] -> add curr ind to stack
        # if not, while curr_height >= stack[-1]: stack.pop() => stack.append(curr_height)
        stack = []  # idx, height

        # 0, 4
        # 2, 3
        # 3, 1

        for ind, h in enumerate(heights):
            if not stack or stack[-1][1] > h:
                stack.append([ind, h])
                continue
            while stack and stack[-1][1] <= h:
                stack.pop()
            stack.append([ind, h])
        
        return [idx for idx, h in stack]

        