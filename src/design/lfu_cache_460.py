from typing import Optional


class CacheNode:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.count = 1
        self.prev: Optional[CacheNode] = None
        self.next: Optional[CacheNode] = None


class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.data = {}
        self.first_count = {}  # the first node with the same counter
        self.head = CacheNode()
        self.tail = self.head

    def get(self, key: int) -> int:
        node: CacheNode = self.data.get(key)
        if node is None:
            return -1
        prev_count = node.count
        node.count += 1

        # move the node to the first node of the nodes with the same count
        first = self.first_count.get(prev_count)
        next_first = self.first_count.get(node.count)
        if next_first is not None:
            target = next_first.prev
        else:
            target = first.prev
        if first == node:
            if first.next is not None and first.next.count == prev_count:
                self.first_count[prev_count] = first.next
            else:
                del self.first_count[prev_count]
        self.first_count[node.count] = node

        # node need to move
        if node.prev == self.head:
            return node.val

        # remove node
        self._remove(node)
        # insert after target node
        self._insert(node, target)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self._modify_node(key, value)
        else:
            self._add_node(key, value)

    def _add_node(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            self.size -= 1
            if self.tail.prev == self.head \
                    or self.tail.prev != self.head and self.tail.prev.count != self.tail.count:
                del self.first_count[self.tail.count]
            del self.data[self.tail.key]
            self._remove(self.tail)

        self.size += 1
        node = CacheNode(key, value)
        first = self.first_count.get(1)
        if first is None:
            target = self.tail
        else:
            target = first.prev
        self.first_count[1] = node
        self.data[key] = node
        self._insert(node, target)
        if target == self.tail:
            self.tail = node

    def _modify_node(self, key: int, value: int) -> None:
        node: CacheNode = self.data.get(key)
        first = self.first_count.get(node.count)
        next_first = self.first_count.get(node.count + 1)

        # find the target node to append the changed node
        if next_first is not None:
            target = next_first.prev
        else:
            target = first.prev

        # find the next first node with the same count
        if first == node:
            if first.next is not None and first.next.count == node.count:
                self.first_count[node.count] = first.next
            else:
                del self.first_count[node.count]

        node.count += 1
        node.val = value
        self.first_count[node.count] = node

        self._remove(node)
        self._insert(node, target)

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
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    # cache = LFUCache(2)
    # cache.put(3, 1)
    # cache.put(2, 1)
    # cache.put(2, 2)
    # cache.put(4, 4)
    # print(cache.get(2))

    # cache = LFUCache(3)
    # cache.put(2, 2)
    # cache.put(1, 1)
    # print(cache.get(2))
    # print(cache.get(1))
    # print(cache.get(2))
    # cache.put(3, 3)
    # cache.put(4, 4)
    # print(cache.get(3))
    # print(cache.get(2))
    # print(cache.get(1))
    # print(cache.get(4))

    # cache = LFUCache(1)
    # cache.put(2, 1)
    # print(cache.get(2))
    # cache.put(3, 2)
    # print(cache.get(2))
    # print(cache.get(3))
