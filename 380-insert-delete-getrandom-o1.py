from random import randint


class RandomizedSet:

    def __init__(self):
        self._list = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False

        self._list.append(val)
        self._dict[val] = len(self._list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False

        i = self._dict[val]
        j = len(self._list) - 1
        self._list[i], self._list[j] = self._list[j], self._list[i]
        self._dict[self._list[i]] = i
        self._dict.pop(val)
        self._list.pop()
        return True

    def getRandom(self) -> int:
        return self._list[randint(0, len(self._list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
