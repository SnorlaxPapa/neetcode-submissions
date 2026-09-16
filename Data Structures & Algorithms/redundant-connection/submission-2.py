class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        disjoint set union -> if two nodes already have a parent that are equal, 
        means if we connect it will form a cycle
        so we don't need this 
        """
        parent = {i: i for i in range(len(edges) + 1)}
        size = {i: 1 for i in range(len(edges) + 1)}

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node_a, node_b):
            root_a = find(node_a)
            root_b = find(node_b)

            if size[root_a] > size[root_b]: 
                parent[root_b] = root_a
                size[root_a] += size[root_b]
            else:
                parent[root_a] = root_b
                size[root_b] += size[root_a]

        candidates = []
        for edge in edges:
            node_a, node_b = edge
            if find(node_a) == find(node_b): 
                candidates.append(edge)
            else:
                union(node_a, node_b)

        return candidates[-1]
