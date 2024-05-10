from typing import List


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    result: List[List[str]] = []
    products.sort()
    filtered = products
    for i in range(len(searchWord)):
        filtered = [w for w in filtered if i < len(w) and w[i] == searchWord[i]]
        result.append(filtered[0:3])
    return result


if __name__ == '__main__':
    print(suggestedProducts(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'))
    print(suggestedProducts(['bags', 'baggage', 'banner', 'box', 'cloths'], 'bags'))
