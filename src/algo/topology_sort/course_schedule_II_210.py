from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_map: dict[int, List[int]] = {}
    degree = [0] * numCourses
    for pre in prerequisites:
        if pre[1] not in adj_map:
            adj_map[pre[1]] = []
        adj_map.get(pre[1]).append(pre[0])
        degree[pre[0]] += 1

    order = []
    q = [c for c in range(numCourses) if degree[c] == 0]
    while len(q) > 0:
        c = q.pop(0)
        order.append(c)
        for n in adj_map.get(c, []):
            degree[n] -= 1
            if degree[n] == 0:
                q.append(n)

    return order if len(order) == numCourses else []


if __name__ == '__main__':
    print(findOrder(2, [[1, 0]]))
    print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(findOrder(1, []))
    print(findOrder(3, [[1, 0], [1, 2], [0, 1]]))
