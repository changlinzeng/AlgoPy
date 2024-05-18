from typing import List


def maxArea(height: List[int]) -> int:
    start, end = 0, len(height) - 1
    max_area = 0
    while start < end:
        area = min(height[start], height[end]) * (end - start)
        max_area = max(max_area, area)
        # find the next greater height on the right
        if height[start] <= height[end]:
            i = start + 1
            while i < end and height[i] <= height[start]:
                i += 1
            start = i
            area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, area)
        # find the next greater height on the left
        if height[end] < height[start]:
            i = end - 1
            while i > start and height[i] <= height[end]:
                i -= 1
            end = i
            area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, area)

    return max_area
