from typing import List


class StockSpanner:

    def __init__(self):
        self.min_stack: List[tuple[int, int]] = []  # list of (stock price, span)

    def next(self, price: int) -> int:
        span = 1
        while len(self.min_stack) > 0 and self.min_stack[-1][0] <= price:
            span += self.min_stack.pop()[1]
        self.min_stack.append((price, span))
        return span
