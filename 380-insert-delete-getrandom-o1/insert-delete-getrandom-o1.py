import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False

        self.mp[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        i = self.mp[val]
        last = self.arr[-1]

        self.arr[i] = last
        self.mp[last] = i

        self.arr.pop()
        del self.mp[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)