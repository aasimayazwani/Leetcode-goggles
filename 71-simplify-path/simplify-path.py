class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        while len(path) > 0:
            if path[0] == "..":
                if len(stack) > 0:
                    stack.pop(-1)
                path.pop(0)
            elif path[0] == "." or path[0] == "":
                path.pop(0)
            else:
                stack.append(path[0])
                path.pop(0)
        return "/" + "/".join(stack)