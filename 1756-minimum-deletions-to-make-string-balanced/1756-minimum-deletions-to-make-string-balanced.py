class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        deletions = 0
        for char in s:
            if stack and stack[-1] == "b" and char == "a":
                stack.pop()
                deletions += 1
            else:
                stack.append(char)
        
        return deletions