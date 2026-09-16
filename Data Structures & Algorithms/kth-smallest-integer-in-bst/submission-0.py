# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        kth smallest. bottom-up solution -> in order traversal. ideally stop iterating at k for O(k) solution

        """

        position = 1
        number = 0

        def dfs(node):
            if node == None: return 
            nonlocal position

            dfs(node.left)
            if position == k: 
                nonlocal number
                number = node.val
            position += 1
            dfs(node.right)

        dfs(root)

        return number