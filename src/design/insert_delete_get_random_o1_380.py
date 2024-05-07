from random import randint


class RandomizedSet:

    def __init__(self):
        self.map = {}  # val -> index of val in lst
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.lst.append(val)
        self.map[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        del self.map[val]
        # move last element to idx and remove the last element
        if idx < len(self.lst) - 1:
            last = self.lst[-1]
            self.lst[idx] = last
            self.map[last] = idx
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        rand = randint(1, len(self.lst))
        return self.lst[rand - 1]
