from typing import List, Set


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    union_find = list(range(len(accounts)))
    email_acct_map: dict[str, int] = {}  # email -> direct account id

    for acct_id, accts in enumerate(accounts):
        for i, email in enumerate(accts):
            if i == 0:
                continue
            if email not in email_acct_map:
                email_acct_map[email] = acct_id
                continue
            # check if the account od this email belongs to current account
            email_acct = email_acct_map[email]
            # merge email account to current account
            if union_find[email_acct] != acct_id:
                parent_acct = union_find[email_acct]
                for j in range(len(union_find)):
                    if union_find[j] == parent_acct:
                        union_find[j] = acct_id

    merge: dict[int, tuple[str, Set[str]]] = {}
    for acct_id, parent_id in enumerate(union_find):
        if parent_id not in merge:
            merge[parent_id] = (accounts[parent_id][0], set(accounts[parent_id][1:]))
        if acct_id != parent_id:
            # merge account to parent
            merge[parent_id] = merge[parent_id][0], merge[parent_id][1].union(accounts[acct_id][1:])

    result = []
    for _, v in merge.items():
        lst = list(v[1])
        lst.sort()
        result.append([v[0]] + lst)
    return result


if __name__ == '__main__':
    print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"], ["John","johnsmith@mail.com","john00@mail.com"], ["Mary","mary@mail.com"], ["John","johnnybravo@mail.com"]]))
