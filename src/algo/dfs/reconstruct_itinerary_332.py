import heapq
from collections import defaultdict
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:

    def _post_order(adj_map: dict[str, List[str]], city: str, itinerary: List[str]) -> None:
        destinations = adj_map.get(city, [])
        while len(destinations) > 0:
            dest = heapq.heappop(destinations)
            _post_order(adj_map, dest, itinerary)
        itinerary.append(city)

    adj_map = defaultdict(lambda: [])
    for ticket in tickets:
        heapq.heappush(adj_map[ticket[0]], ticket[1])

    itinerary = []
    _post_order(adj_map, 'JFK', itinerary)
    itinerary.reverse()
    return itinerary


if __name__ == '__main__':
    print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
