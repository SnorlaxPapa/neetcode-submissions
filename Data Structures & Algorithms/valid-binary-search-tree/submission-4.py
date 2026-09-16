# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        we can validate a binary search tree by doing a bfs scan of the tree
        for each node, 

        the problem with doing a local check is the fact that we are not taking account paths above that
        while 3 might be less than its parent node 6, if the parent node is 5, and 6 is on the right side of 5, it will be wrong
        instead, along with the curr val, we should save a min_val/max_val to follow
        for all left side values, the minimum value it must be less thn is the minimum value it encounters along the path
        for all right side values, the max value it must be greater than is the max value on the right side

        what if its left -> right. its max value is still capped at the min_value which is what we saved

        to make the check simple, we can save the tuple as
        (node, min value it must have, max value it can have)
        """

        queue = deque([(root, float("-inf"), float("inf"))]) 

        while queue:
            curr = queue.pop()
            if curr[0]:
                #we check if it is outside this range
                if curr[0].val <= curr[1] or curr[0].val >= curr[2]:
                    return False
                #we append left and right values. for left, the new maximum is the current curr, and for right, the new minimum is the current curr
                queue.append((curr[0].left, curr[1], curr[0].val))
                queue.append((curr[0].right, curr[0].val, curr[2]))

        return True
