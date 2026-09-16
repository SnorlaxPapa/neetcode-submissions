import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        single-source djikstra
        as we iterate through times,
        we must take note of the folloing:
        which nodes are source nodes 

        we must concurrently set up a directed adjacency list with source node: [(target_node, cost)]

        we then conduct single-source search with djikstra's starting from K. why djikstra? because it is a weighted graph, and the min-heap allows us to find the shortest distance to the relevant nodes

        time complexity. 
        if there are E nodes and V vertices, total V num items O(V) time. adj list is O(V+E) space
        in djikstra's, for V vertices, each insertion takes log(V) time. we do E number of insertions so time O(ElogV)
        """

        adj = {i: [] for i in range(1, n+1)}
        dist = [float("inf") for i in range(n)]
        for triplet in times:
            source, target, time = triplet

            #adjust distance and adj list of source
            adj[source].append((time, target))

        min_heap = [(0, k)]
        reached = 0
        dist[k - 1] = 0

        reached = 1
        while min_heap:
            curr_time, curr = heapq.heappop(min_heap)
            if curr_time > dist[curr - 1]: continue

            for time, neighbor in adj[curr]:
                new_dist = time + curr_time
                if new_dist >= dist[neighbor - 1]:
                    continue
                
                if dist[neighbor - 1] == float("inf"): reached += 1
                dist[neighbor - 1] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

        if reached != n: return -1

        min_time = float("-inf")
        for distance in dist:
            min_time  = max(min_time, distance)

        return min_time
        


