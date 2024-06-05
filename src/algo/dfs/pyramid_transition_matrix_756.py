from collections import defaultdict
from typing import List


def pyramidTransition(bottom: str, allowed: List[str]) -> bool:
    def _generate_row(row: str, allowed: dict[str, List[str]], memo: dict[str, List[str]]) -> List[str]:
        if len(row) < 2:
            return []
        key = f'{row[0]}_{row[1]}'
        if row in memo:
            return memo[row]
        if key not in allowed:
            return []
        if len(row) == 2:
            return allowed_dict[key]
        res = []
        next_rows = _generate_row(row[1:], allowed, memo)
        if len(next_rows) > 0:
            for next_char in allowed[key]:
                for r in next_rows:
                    res.append(next_char + r)
            memo[row] = res
        return res

    allowed_dict = defaultdict(lambda: [])
    for p in allowed:
        allowed_dict[f'{p[0]}_{p[1]}'].append(p[2])

    memo = defaultdict(lambda: [])
    visited = set()
    q = [bottom]
    while len(q) > 0:
        row = q.pop(0)
        if row in visited:
            continue
        visited.add(row)
        for r in _generate_row(row, allowed_dict, memo):
            if len(r) == 1:
                return True
            q.append(r)
    return False


if __name__ == '__main__':
    # print(pyramidTransition('BCD', ["BCC", "CDE", "CEA", "FFF"]))
    # print(pyramidTransition('AAAA', ["AAB", "AAC", "BCD", "BBE", "DEF"]))
    # print(pyramidTransition('AABA', ["AAA","AAB","ABA","ABB","BAC"]))
    # print(pyramidTransition('CBDDA', ["ACC","ACA","AAB","BCA","BCB","BAC","BAA","CAC","BDA","CAA","CCA","CCC","CCB","DAD","CCD","DAB","ACD","DCA","CAD","CBB","ABB","ABC","ABD","BDB","BBC","BBA","DDA","CDD","CBC","CBA","CDA","DBA","ABA"]))
    # TODO Timeout!!
    print(pyramidTransition('FDBACE', [["EEF","BFE","EDD","EFB","EFC","DCE","CCE","ABB","BBB","EDC","ADD","AFE","CAF","DEF","ABE","BBD","CBB","ADB","ABD","EDF","FAE","CAA","CFB","BCA","BDC","EAB","FFE","FBF","EFF","AFD","DFA","BED","BDD","ABA","FCB","CBD","CDC","CEC","ECC","ECA","EBC","DFD","FFB","BDE","DBD","EBB","DEB","BEF","FFA","AEA","CCC","BFF","DCD","BBA","CFF","ECD","CBF","CCD","FAA","EDA","ADF","ECE","FCF","FFF","FCE","BFC","CCF","ACD","FDB","DBA","AED","FDD","BDF","FBE","DCB","ACE","FBC","FEF","FDF","AEF","DDB","CFA","BCB","EFA","EAC","FBD","CFC","AEE","CEB","AFA","CCA","BFD","BAC","BAA","CEE","DAB","AFC","DBE","BEE","DAF","DCA","EEA","BDB","EEB","EAA","BEC","DED","CDE","CDB","EEE","DAC","EBF","EBD","FDE","ABC","ACB","DBC","FBA","BAE","EFE","BBC","CBC","FED","FEA","ACF","DCF","FDA","BCC","ADE","DAE","DCC","EDB","AFB","CEA","DFE","BAD","FEC","EEC","EBE","CEF","EAD","ABF","EFD","AAB","AAD","FAB","FEE","CBE","BBE","ADC","FAD","DBB","CAB","CDA","AAF","DBF","FCA","DEE","EDE","FFC","DDD","DDA","DEC","DFF","BCD","ECF","DDF","AEB","BDA","FBB","BCE","DAA","ACC","CCB","FAC","BAF","BEA","CFD","EBA","ACA","DAD","BFB","ECB","CAD","DDC","FCC","BEB","FAF","BBF","AAA","AAC","CED","AAE","CDD","DDE","DEA","FFD","DFC","CFE","FEB","FDC","ADA","BCF","AFF","EAE","AEC","CAC","CDF","BAB","EED","CAE","FCD","BFA","EAF","CBA","DFB"]]))
