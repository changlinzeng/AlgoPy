from collections import defaultdict
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    degree = [0] * numCourses
    adj_map: dict[int, List[int]] = defaultdict(lambda: [])
    for pre in prerequisites:
        adj_map[pre[1]].append(pre[0])
        degree[pre[0]] += 1

    q = []
    for i, v in enumerate(degree):
        if v == 0:
            q.append(i)

    visited = set()
    while len(q) > 0:
        course = q.pop(0)
        if course in visited:
            return False
        visited.add(course)
        for nxt in adj_map[course]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

    return len(visited) == numCourses
