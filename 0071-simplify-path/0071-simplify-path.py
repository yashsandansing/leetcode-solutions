class Solution:
    def simplifyPath(self, path: str) -> str:
        ind = 0
        stack = []

        while ind<len(path):
            curr = ""
            while ind<len(path) and path[ind]!="/":
                curr+=path[ind]
                ind+=1
            if curr:
                if curr == "..":
                    if stack:
                        stack.pop()
                    continue
                elif curr == ".":
                    continue
                else:
                    stack.append(curr)
            while ind<len(path) and path[ind] == "/":
                ind+=1
        return "/" + '/'.join(i for i in stack)