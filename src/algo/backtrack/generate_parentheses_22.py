from typing import List


def generateParenthesis(n: int) -> List[str]:
    def _backtrack(left_count: int, right_count: int, paren: str, parens: List[str]) -> None:
        if left_count == 0 and right_count == 0:
            parens.append(paren)
            return
        if left_count > 0:
            _backtrack(left_count - 1, right_count, paren + '(', parens)
        if right_count > left_count:
            _backtrack(left_count, right_count - 1, paren + ')', parens)

    result = []
    _backtrack(n, n, '', result)
    return result


if __name__ == '__main__':
    print(generateParenthesis(3))
    print(generateParenthesis(2))
    print(generateParenthesis(1))
