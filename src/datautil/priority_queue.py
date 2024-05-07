import heapq
from typing import TypeVar, List

T = TypeVar('T')


class PriorityQueue:
    def __init__(self):
        self.q: List[T] = []

    def offer(self, val: T):
        heapq.heappush(self.q, val)

    def poll(self) -> T:
        return heapq.heappop(self.q)

    def peek(self) -> T:
        return self.q[0]

    def is_empty(self) -> bool:
        return len(self.q) == 0

    def size(self) -> int:
        return len(self.q)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.offer(3)
    pq.offer(2)
    pq.offer(5)
    print(pq.poll())
    print(pq.poll())
    print(pq.poll())
