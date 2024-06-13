from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    max_len = 0
    zero_count = 0
    left, right = 0, 0
    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1
        while left < right and zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        if zero_count <= k:
            max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


if __name__ == '__main__':
    print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
