import heapq
from collections import defaultdict
from typing import List


class FreqStack:

    class Node:
        def __init__(self, val: int, seq: int, freq: int = 1):
            self.val = val
            self.seq = seq
            self.count = freq

        def __lt__(self, other):
            if self.count == other.count:
                return self.seq > other.seq
            return self.count > other.count

    def __init__(self):
        self.freq: dict[int, int] = defaultdict(lambda: 0)  # val -> freq
        self.data: List[FreqStack.Node] = []
        self.seq = 0

    def push(self, val: int) -> None:
        self.seq += 1
        self.freq[val] += 1
        node = FreqStack.Node(val, self.seq, self.freq[val])
        heapq.heappush(self.data, node)

    def pop(self) -> int:
        node = heapq.heappop(self.data)
        self.freq[node.val] -= 1
        return node.val


if __name__ == '__main__':
    mf_stack = FreqStack()
    mf_stack.push(5)
    mf_stack.push(7)
    mf_stack.push(5)
    mf_stack.push(7)
    mf_stack.push(4)
    mf_stack.push(5)
    print(mf_stack.pop())
    print(mf_stack.pop())
    print(mf_stack.pop())
    print(mf_stack.pop())
