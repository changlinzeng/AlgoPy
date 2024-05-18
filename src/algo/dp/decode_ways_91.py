from typing import List


def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    dp: List[int] = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i - 1] in ['1', '2']:
                if i > 1:
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 1
        else:
            if s[i - 1] == '1' or s[i - 1] == '2' and '1' <= s[i] <= '6':
                if i > 1:
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = 2
            else:
                dp[i] = dp[i - 1]
    return dp[-1]


if __name__ == '__main__':
    print(numDecodings('12'))
    print(numDecodings('226'))
    print(numDecodings('10'))
    print(numDecodings('2101'))
    print(numDecodings('1123'))
