import heapq
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] != 0:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1,], [1, 0], [1, -1], [0, -1], [-1, -1]]
    distance = {'0_0': 0}  # shortest path from [0, 0] to cell [i, j]
    pq = [(0, '0_0')]
    visited = set()
    while len(pq) > 0:
        cell: str = heapq.heappop(pq)[1]
        if cell in visited:
            continue
        visited.add(cell)
        row, col = int(cell.split('_')[0]), int(cell.split('_')[1])
        for direct in directions:
            next_row, next_col = row + direct[0], col + direct[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0:
                key = f'{next_row}_{next_col}'
                if key in distance:
                    min_dist = min(distance[key], distance[f'{row}_{col}'] + 1)
                    distance[key] = min_dist
                else:
                    distance[key] = distance[f'{row}_{col}'] + 1
                heapq.heappush(pq, (distance[key], key))
    return distance.get(f'{rows - 1}_{cols - 1}', -2) + 1


if __name__ == '__main__':
    print(shortestPathBinaryMatrix([[0, 1], [1, 0]]))
