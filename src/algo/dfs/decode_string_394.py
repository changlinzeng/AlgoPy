def decodeString(s: str) -> str:
    def _decode(s: str, start: int) -> tuple[str, int]:
        num = 0
        decoded = ''
        i = start
        while i < len(s):
            c = s[i]
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            elif 'a' <= c <= 'z':
                decoded += c
            elif c == '[':
                result = _decode(s, i + 1)
                decoded += result[0] * num
                i = result[1]
                num = 0
            elif c == ']':
                break
            i += 1
        return decoded, i
    return _decode(s, 0)[0]


if __name__ == '__main__':
    print(decodeString('3[a]2[bc]'))
