# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return [0, True]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            return [max(left[0], right[0]) + 1, balanced]

            
        return dfs(root)[1]
        

