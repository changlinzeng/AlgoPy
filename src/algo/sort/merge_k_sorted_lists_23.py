from typing import List, Optional

from datautil.linkedlist import ListNode, LinkedList


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def _merge(target: ListNode, lst: ListNode) -> ListNode:
        _tail = target
        i, j = target.next, lst
        while i is not None and j is not None:
            if i.val <= j.val:
                _tail.next = i
                i = i.next
            else:
                _tail.next = j
                j = j.next
            _tail = _tail.next
        while i is not None:
            _tail.next = i
            _tail = _tail.next
            i = i.next
        while j is not None:
            _tail.next = j
            _tail = _tail.next
            j = j.next
        return target

    head = ListNode()
    for lst in lists:
        head = _merge(head, lst)
    return head.next if head is not None else None


if __name__ == '__main__':
    list1 = LinkedList.from_list([1, 4, 5])
    list2 = LinkedList.from_list([1, 3, 4])
    print(mergeKLists([list1, list2]))
