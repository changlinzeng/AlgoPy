import heapq
from typing import List


def longestDiverseString(a: int, b: int, c: int) -> str:
    pq: List[tuple[str, int]] = []
    if a > 0:
        heapq.heappush(pq, (-1 * a, 'a'))
    if b > 0:
        heapq.heappush(pq, (-1 * b, 'b'))
    if c > 0:
        heapq.heappush(pq, (-1 * c, 'c'))

    happy = ''
    while len(pq) > 0:
        count, ch = heapq.heappop(pq)
        if len(happy) > 1 and happy[-2:] == ch * 2:
            if len(pq) == 0:
                return happy
            count2, ch2 = heapq.heappop(pq)
            happy += ch2
            count2 += 1
            heapq.heappush(pq, (count, ch))
            if count2 < 0:
                heapq.heappush(pq, (count2, ch2))
        else:
            consume = 2
            if len(happy) > 0 and happy[-1] == ch:
                consume = 1
            happy += ch * min(-1 * count, consume)
            count += consume
            if count < 0:
                heapq.heappush(pq, (count, ch))
    return happy


if __name__ == '__main__':
    print(longestDiverseString(1, 1, 7))
