from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        answer = []

        while queue:

            current = queue.popleft()

            if valid(current):
                answer.append(current)

            # If we already found valid answers,
            # don't remove more characters
            if answer:
                continue

            for i in range(len(current)):

                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return answer