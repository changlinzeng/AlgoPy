from typing import List


def restoreIpAddresses(s: str) -> List[str]:

    def _backtrack(s: str, start: int, addr: List[str], ips: List[str]) -> None:
        if len(addr) > 4:
            return
        if start == len(s):
            if len(addr) == 4:
                ips.append('.'.join(addr))
            return
        part = ''
        for i in range(start, len(s)):
            part += s[i]
            if part == '0':
                # single '0'
                addr.append(part)
                _backtrack(s, i + 1, addr, ips)
                addr.pop()
                break
            if int(part) > 255:
                break
            addr.append(part)
            _backtrack(s, i + 1, addr, ips)
            addr.pop()

    ips = []
    _backtrack(s, 0, [], ips)
    return ips


if __name__ == '__main__':
    print(restoreIpAddresses('25525511135'))
    print(restoreIpAddresses('0000'))
    print(restoreIpAddresses('101023'))
