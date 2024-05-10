from typing import List


def letterCombinations(digits: str) -> List[str]:
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def _backtrack(digits: str, index: int, combination: str, combinations: List[str]) -> None:
        for c in digit_map[digits[index]]:
            if index == len(digits) - 1:
                combinations.append(combination + c)
            else:
                _backtrack(digits, index + 1, combination + c, combinations)

    if digits == '':
        return []
    combinations = []
    _backtrack(digits, 0, '', combinations)
    return combinations


if __name__ == '__main__':
    print(letterCombinations('23'))
    print(letterCombinations(''))
