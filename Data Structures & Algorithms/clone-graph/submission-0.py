"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        copies = {}
        new_head = Node(node.val)

        def copy(original_node, new_node):
            """
            iterate and check through neighbors.
            if alr exists, use that node, if not, create a new node and recursively copy that
            """
            for neighbor in original_node.neighbors:
                if neighbor.val in copies: 
                    new_node.neighbors.append(copies[neighbor.val])
                    continue

                #create copy, recursively clone
                new_neighbor = Node(neighbor.val)
                copies[new_neighbor.val] = new_neighbor
                copy(neighbor, new_neighbor)

                #append to neighbor and copies
                new_node.neighbors.append(new_neighbor)

        copies[new_head.val] = new_head
        copy(node, new_head)

        return new_head
