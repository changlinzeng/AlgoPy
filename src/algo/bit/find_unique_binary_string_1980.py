from typing import List


def findDifferentBinaryString(nums: List[str]) -> str:
    def _bin_str_to_num(s: str) -> int:
        num = 0
        for i in reversed(range(len(s))):
            # '1010'
            n = len(s)
            if s[i] == '1':
                num += (1 << (n - i - 1))
        return num

    uniq = set()
    for num in nums:
        uniq.add(_bin_str_to_num(num))

    n = len(nums[0])
    for i in range(1 << 17):
        if i not in uniq:
            return bin(i)[2:].zfill(n)


if __name__ == '__main__':
    print(findDifferentBinaryString(['111', '011', '001']))
