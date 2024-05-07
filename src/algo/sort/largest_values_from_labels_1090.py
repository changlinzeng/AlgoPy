from collections import defaultdict
from typing import List


def largestValsFromLabels(values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    labeled_values = []
    for v, l in zip(values, labels):
        labeled_values.append((v, l))

    labeled_values.sort(key=lambda a: a[0], reverse=True)

    label_count = defaultdict(lambda: 0)
    score = 0
    num_limit = numWanted
    for val in labeled_values:
        lbl = val[1]
        if label_count[lbl] < useLimit:
            label_count[lbl] += 1
            score += val[0]
            num_limit -= 1
            if num_limit == 0:
                break
    return score


if __name__ == '__main__':
    print(largestValsFromLabels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1))
