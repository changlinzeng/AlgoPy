from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    # find the section with odd number of elements
    while start <= end:
        if start == end:
            return nums[start]
        mid = start + (end - start) // 2
        # find it
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if nums[mid] == nums[mid - 1]:
            # there are even number of elements in front
            if (mid - start + 1) % 2 == 0:
                start = mid + 1
            else:
                end = mid
        elif nums[mid] == nums[mid + 1]:
            # there are even number of elements in end
            if (end - mid + 1) % 2 == 0:
                end = mid - 1
            else:
                start = mid


if __name__ == '__main__':
    print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 10, 11]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
