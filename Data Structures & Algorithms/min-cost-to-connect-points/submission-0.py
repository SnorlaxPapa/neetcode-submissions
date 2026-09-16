import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        construct MST with prim's algorithm
        need to first find all edges between points O(n^2) and create adjacency list
        store as (distance, index of point) in adjacency list

        we push a random point to heap
        then, as we pop the current one, we add all its neighbors to the heap if they have not yet been visited, and we mark the current one as visited
        once we have visited all points (length of visited == points), then we have formed complete MST 
        bidirectional
        """

        adj = {i: [] for i in range(len(points))}        
        heap = [(0, 0)]

        #create edges
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            for j in range(i+1, len(points)):
                neighbor_x, neighbor_y = points[j]
                manhattan = abs(curr_x - neighbor_x) + abs(curr_y - neighbor_y)

                adj[i].append((manhattan, j)) 
                adj[j].append((manhattan, i))
        
        visited = set()
        total = 0
        while len(visited) != len(points):
            distance, idx = heapq.heappop(heap)
            if idx in visited: continue
            
            visited.add(idx)
            total += distance

            for manhattan, idx in adj[idx]:
                if idx in visited: continue
                heapq.heappush(heap, (manhattan, idx))

        return total