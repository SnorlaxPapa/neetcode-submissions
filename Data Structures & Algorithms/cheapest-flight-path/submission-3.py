import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        djikstra. but with path limitation, we add data in form (distance, path count, airport)
        once path count hits k, we stop appending
        """

        adj = {i: [] for i in range(n)}

        for flight in flights:
            frm, to, price = flight
            adj[frm].append((price, to))

        min_heap = [(0, -1, src)]
        min_stops = {}

        while min_heap:
            curr_cost, curr_path, port = heapq.heappop(min_heap)

            if port == dst and curr_path <= k + 1: return curr_cost
            if port in min_stops and min_stops[port] <= curr_path: continue
            min_stops[port] = curr_path

            if curr_path + 1 > k : continue

            for neighbour in adj[port]:
                cost, to = neighbour
                heapq.heappush(min_heap, (curr_cost + cost, curr_path + 1, to))

        return -1


