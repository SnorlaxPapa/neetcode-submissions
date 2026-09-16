# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        intuitively, if we do a preorder traversal with DFS and within each DFS function tracking the maximal value seen at this stage        

        so at each step, we check if the node is greater than our maximum value. if it is, we add one to our nonlocal counter
        additionally, we pass in this new maximum value as the dfs max for paths after this node
        """

        count = 0
        def dfs(node, max_value):
            nonlocal count

            if node == None: return

            if node.val >= max_value:
                count += 1
                max_value = node.val
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, float("-inf"))
        return count