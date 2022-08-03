class DLLNode:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

    def __repr__(self):
        return self.__str__()


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        self.__update_recent(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if self.head is None:
            self.head = self.tail = self.map[key] = DLLNode(key, value)

        elif key in self.map:
            self.map[key].val = value
            self.__update_recent(self.map[key])

        else:
            self.tail.next = self.map[key] = DLLNode(key, value, self.tail)
            self.tail = self.tail.next
            if len(self.map) > self.capacity:
                self.map.pop(self.head.key)
                self.head = self.head.next
                self.head.prev = None

    def __update_recent(self, node):
        if self.head == self.tail or node == self.tail:
            return

        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None

        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.next = node.prev = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


if __name__ == '__main__':
    l = LRUCache(2)
    assert l.get(1) == -1
    l.put(1, 1)
    l.put(2, 2)
    assert l.get(1) == 1
    assert l.get(2) == 2

    l.put(3, 3)
    assert l.get(1) == -1
    assert l.get(2) == 2
    l.put(4, 4)
    assert l.get(3) == -1
    assert l.get(2) == 2
    assert l.get(4) == 4
