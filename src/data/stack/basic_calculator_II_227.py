def calculate(s: str) -> int:
    nums = []
    num = None
    operator = '+'
    for c in s + ' ':  # append space to the end so we can process all the nums
        if '0' <= c <= '9':
            if num is None:
                num = 0
            num = num * 10 + int(c)
        else:
            if operator is not None and num is not None:
                if operator == '+':
                    nums.append(num)
                elif operator == '-':
                    nums.append(-1 * num)
                elif operator == '*':
                    nums[-1] = nums[-1] * num
                elif operator == '/':
                    if nums[-1] < 0:
                        nums[-1] = -1 * (abs(nums[-1]) // num)
                    else:
                        nums[-1] = nums[-1] // num
                num = None
            if c in ['+', '-', '*', '/']:
                operator = c
    return sum(nums)


if __name__ == '__main__':
    print(calculate('3+2*2'))
    print(calculate('  3/ 2 '))
    print(calculate('  3+5 / 2 '))
    print(calculate('0-2147483647'))
    print(calculate('2*3-4'))
    print(calculate('14-3/2'))
    print(calculate('2995-9/3*3*3-138*9'))
