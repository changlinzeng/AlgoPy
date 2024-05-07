from typing import Optional, List


class ListNode:
    def __init__(self, val: int = None):
        self.val = val
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    @staticmethod
    def from_list(lst: Optional[List[int]]) -> ListNode:
        _head = ListNode()
        _tail = _head
        if lst is None:
            return _head
        for e in lst:
            _tail.next = ListNode(e)
            _tail = _tail.next
        return _head.next
