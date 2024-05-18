def solveEquation(equation: str) -> str:
    left_coefficient, right_coefficient = 0, 0
    left_num, right_num = 0, 0
    num, sign = None, 1
    left_side = True
    for c in equation + '+':
        if c == '=':
            if num is not None:
                left_num += sign * num
            left_side = False
            sign = 1
            num = None
            continue
        if '0' <= c <= '9':
            if num is None:
                num = 0
            num = num * 10 + ord(c) - ord('0')
        elif c == 'x':
            if num is None:
                num = 1
            if left_side:
                left_coefficient += sign * num
            else:
                right_coefficient += sign * num
            num = None
        else:
            if num is not None:
                if left_side:
                    left_num += sign * num
                else:
                    right_num += sign * num
            num = None
            sign = 1
            if c == '-':
                sign = -1

    num = right_num - left_num
    coefficient = left_coefficient - right_coefficient
    if coefficient == 0:
        if num == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
    return f'x={num // coefficient}'


if __name__ == '__main__':
    print(solveEquation('x+5-3+x=6+x-2'))
    print(solveEquation('2x=x'))
    print(solveEquation('x=x'))
    print(solveEquation('2x+3x-6x=x+2'))
    print(solveEquation('1+1=x'))
    print(solveEquation('2=-x'))
    print(solveEquation('0x=0'))
