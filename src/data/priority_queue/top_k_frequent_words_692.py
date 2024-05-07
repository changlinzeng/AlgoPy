import heapq
from collections import defaultdict
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    count = defaultdict(lambda: 0)
    for word in words:
        count[word] += 1

    pq = []
    for key, val in count.items():
        heapq.heappush(pq, (-val, key))

    top_k = []
    for _ in range(k):
        top_k.append(heapq.heappop(pq))

    top_k.sort(key=lambda item: (item[0], item[1]))
    return [x[1] for x in top_k]


if __name__ == '__main__':
    print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
