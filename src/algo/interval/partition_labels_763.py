from collections import defaultdict
from typing import List


def partitionLabels(s: str) -> List[int]:
    """
    find the first and last occurrence of each character as [start, end] and then merge the overlapped intervals
    :param s: string to partition
    :return: list of the length of intervals
    """
    char_index = defaultdict(lambda: [-1, -1])
    for i in range(len(s)):
        c = s[i]
        if char_index[c][0] == -1:
            char_index[c][0] = i
        char_index[c][1] = i

    intervals = [t for t in char_index.values()]
    intervals.sort()
    start, end = -1, -1
    partitions = []
    for interval in intervals:
        if start == -1:
            start, end = interval[0], interval[1]
        else:
            if end < interval[0]:
                partitions.append(end - start + 1)
                start, end = interval[0], interval[1]
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
    partitions.append(end - start + 1)
    return partitions


if __name__ == '__main__':
    print(partitionLabels('ababcbacadefegdehijhklij'))
