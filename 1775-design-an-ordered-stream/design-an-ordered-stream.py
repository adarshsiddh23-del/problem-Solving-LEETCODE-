class OrderedStream:

    def __init__(self, n):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey, value):
        self.stream[idKey] = value
        ans = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            ans.append(self.stream[self.ptr])
            self.ptr += 1

        return ans