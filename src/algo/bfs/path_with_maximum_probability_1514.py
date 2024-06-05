import heapq
from collections import defaultdict
from typing import List


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    """ Dijkstra algorithm to find the greatest path
    """
    adj_map: dict[int, List[tuple[int, float]]] = defaultdict(lambda: [])
    for i, edge in enumerate(edges):
        adj_map[edge[0]].append((edge[1], succProb[i]))
        adj_map[edge[1]].append((edge[0], succProb[i]))

    prob: List[float] = [0] * n
    prob[start_node] = 1
    visited = [False] * n
    q = [(-1, start_node)]  # tuple of prob and node
    while len(q) > 0:
        _, cur_node = heapq.heappop(q)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for nxt in adj_map[cur_node]:
            next_node, next_pro = nxt
            prob[next_node] = max(prob[next_node], prob[cur_node] * next_pro)
            heapq.heappush(q, (-1 * prob[next_node], next_node))
    return prob[end_node]
