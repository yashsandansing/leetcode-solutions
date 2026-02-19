class Solution:
    def simplifyPath(self, path: str) -> str:
        # no trailing slashes
        # if .. => remove the prev element (if exists)
        # if . => dont add anything
        # return at least / to /path
        
        # empty list -> return /
        # stack -> .. pop from the stack
        # . -> dont add anything
        # /.join(stack)

        path = path.split("/")
        print(path)
        stack = []

        for loc in path:
            if loc == "." or not loc:
                continue
            elif loc == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(loc)
        
        return "/" + "/".join(stack)