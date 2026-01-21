class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_count = {c: i for i,c in enumerate(s)}
        visit = set()

        for ind in range(len(s)):
            if s[ind] not in visit:
                while stack and stack[-1] > s[ind]:
                    prev = stack[-1]
                    if last_count[prev] > ind:
                        stack.pop()
                        visit.remove(prev)
                    else:
                        break
        
                stack.append(s[ind])
                visit.add(s[ind])
        
        return "".join(stack)