class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        disjoint set?

        when given two edges,
        we use a union function to combine them. then we find the number of unique parents among all our nodes
        """
        parent = {i: i for i in range(n)}
 
        def find(node):
            if parent[node] == node:
                return node

            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node_a, node_b):
            root_a = find(node_a)
            root_b = find(node_b)

            if root_a == root_b: return

            parent[root_b] = root_a

        for node_a, node_b in edges:
            union(node_a, node_b)

        unique_graphs = set()
        for node, par in parent.items():
            root = find(node)
            if root not in unique_graphs:
                unique_graphs.add(root)

        return len(unique_graphs)
