class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (char, count)
        for c in s:
            # print(c, stack)
            if not stack:
                stack.append([c, 1])
                continue
            
            if c == stack[-1][0]:
                if stack[-1][1] == k:
                    stack[-1][1] = 1
                else:
                    stack[-1][1] += 1
                continue
            
            else:
                if stack[-1][1] >= k:
                    stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
            
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            
            else:
                if stack[-1][1] == k:
                    stack[-1][1] = 1
                else:
                    stack[-1][1] += 1
        # print(stack, '-')
        if stack[-1][1] >= k:
            stack[-1][1] -= k
            if stack[-1][1] == 0:
                stack.pop()
        # print(stack)
        res = ""
        for (c, i) in stack:
            res += i*c
        return res