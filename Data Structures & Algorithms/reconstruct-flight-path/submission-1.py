from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        use every edge exactly once in alphabetical order
        so we start from edges with no outgoing arrows, then we work backwards in a dfs manner
        """

        adj = {}
        tickets.sort(key=lambda x: x[1])

        for source, to in tickets:
            if source not in adj:
                adj[source] = deque([])
            if to not in adj:
                adj[to] = deque([])

            adj[source].append(to)

        path = []
        def dfs(node):
            while adj[node]:
                to = adj[node].popleft()
                dfs(to)
            path.append(node)
        
        dfs("JFK")
        return path[::-1]