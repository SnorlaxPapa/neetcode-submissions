# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    key part of serializing and deserializing a binary tree is a standardized way of traversal
    i will implement serialization with preorder traversal, separating nodes with $ and including None nodes as none. 
    for encoding, i will join the nodes with $
    For decoding, i will split with $ and use a list to grab the calculated index

    How does index map in pre-order traversal? that is, given an element index i, how do we find its children
    since we save all None children in the tree
    this means the tree is perfectly balanced
    the elements .left is the next element in the list. 
    so we can recursively pop the left tokens until we hit a None
    then recursively pop the right tokens until we hit a None
    """
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder traversal of tree
        string = []

        def dfs(node):
            nonlocal string
            if node is None: 
                string.append("!")
                return

            string.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "$".join(string)
        
    # Decodes your encoded data to tree.
    from collections import deque
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #given a string, we split it into a list and recursively 
        data = deque(data.split("$"))

        def constructTree():
            nonlocal data
            curr = data.popleft()
            if curr == "!": 
                return None

            node = TreeNode(curr) 
            node.left = constructTree()
            node.right = constructTree()

            return node

        return constructTree()
