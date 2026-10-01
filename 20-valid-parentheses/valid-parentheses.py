class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False

                if (c == ')' and stack[-1] != '(') or \
                   (c == ']' and stack[-1] != '[') or \
                   (c == '}' and stack[-1] != '{'):
                    return False

                stack.pop()

        return len(stack) == 0