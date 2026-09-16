from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #construct adjacency list
        adj = {i: [] for i in range(n)}
        for node_one, node_two in edges:
            adj[node_one].append(node_two)
            adj[node_two].append(node_one)

        #start from node 0 and traverse whole graph. item structure of (node, parent)
        visited = {0}
        processed = 0
        queue = deque([(0, None)])

        while queue:
            node, parent = queue.popleft()
            processed += 1

            #iterate through neighbors and check for cycles. 
            for neighbor in adj[node]:
                if neighbor == parent: continue
                if neighbor in visited: return False

                #no cycle, update visited and queue
                visited.add(neighbor)
                queue.append((neighbor, node))

        if processed < n: return False

        return True

