# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        bfs
        we do a level by level comparison. for each curr, we check if the left and right are equal

        we maintain a queue for breadth first search, and a level for the current level's node
        we must maintain None
        we must check that the left and right values are equals to each other and that current values are equals to each other
        """

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False