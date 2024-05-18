from collections import defaultdict
from typing import List


def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    count = 0

    def _bfs(adj_map: dict[int, List[int]], node: int, visited: List[int]) -> None:
        nonlocal count
        node_count, edge_count = 0, 0
        q: List[int] = [node]
        while len(q) > 0:
            e = q.pop()
            if visited[e]:
                continue
            visited[e] = True
            node_count += 1
            for c in adj_map.get(e, []):
                edge_count += 1
                q.append(c)

        edge_count //= 2
        if edge_count == node_count * (node_count - 1) // 2:
            count += 1

    adj_map = defaultdict(lambda: [])
    for edge in edges:
        adj_map[edge[0]].append(edge[1])
        adj_map[edge[1]].append(edge[0])

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            _bfs(adj_map, i, visited)
    return count


if __name__ == '__main__':
    print(countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
