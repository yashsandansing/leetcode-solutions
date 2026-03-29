class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TC: O(N)
        # SC: O(N)
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)