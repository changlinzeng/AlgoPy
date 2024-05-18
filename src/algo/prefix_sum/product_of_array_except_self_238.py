from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    nums_len = len(nums)
    prefix_product = [1] * nums_len
    prefix_product[0] = nums[0]
    for i in range(1, nums_len):
        prefix_product[i] = prefix_product[i - 1] * nums[i]

    suffix_product = [1] * nums_len
    suffix_product[-1] = nums[-1]
    for i in reversed(range(nums_len - 1)):
        suffix_product[i] = suffix_product[i + 1] * nums[i]

    product = [1] * nums_len
    product[0] = suffix_product[1]
    product[-1] = prefix_product[-2]
    for i in range(1, nums_len - 1):
        product[i] = prefix_product[i - 1] * suffix_product[i + 1]

    return product


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
