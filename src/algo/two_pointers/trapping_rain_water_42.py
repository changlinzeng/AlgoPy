from typing import List


def trap(height: List[int]) -> int:
    """
    find the max value on the right of i and the max value on the right of i
    the trapped water at i is determined by the min of left max and right max
    """
    left_max = [-1] * len(height)
    left_max[0] = 0
    max_idx = 0
    for i in range(1, len(height)):
        if height[i] > height[max_idx]:
            max_idx = i
        left_max[i] = max_idx

    right_max = [-1] * len(height)
    right_max[-1] = len(height) - 1
    max_idx = len(height) - 1
    for i in range(len(height) - 2, 0, -1):
        if height[i] > height[max_idx]:
            max_idx = i
        right_max[i] = max_idx

    trapped = 0
    for i in range(1, len(height) - 1):
        h = min(height[left_max[i]], height[right_max[i]])
        trapped += h - height[i]
    return trapped


if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([4, 2, 3]))
