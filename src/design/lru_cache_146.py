from typing import Optional


class CacheNode:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next: Optional[CacheNode] = None
        self.prev: Optional[CacheNode] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.head = CacheNode()
        self.tail = self.head

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if node is None:
            return -1
        if self.head.next != node:
            self._remove(node)
            self._insert(node, self.head)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node is not None:
            node.val = value
            self._remove(node)
        else:
            self.size += 1
            node = CacheNode(key, value)
            self.data[key] = node

        self._insert(node, self.head)

        if self.size > self.capacity:
            self.size -= 1
            del self.data[self.tail.key]
            self._remove(self.tail)

    def _remove(self, node: CacheNode) -> None:
        prev = node.prev
        if node == self.tail:
            self.tail = prev
        prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _insert(self, node: CacheNode, target: CacheNode) -> None:
        if target == self.tail:
            self.tail = node
        node.next = target.next
        node.prev = target
        target.next = node
        if node.next is not None:
            node.next.prev = node


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))
