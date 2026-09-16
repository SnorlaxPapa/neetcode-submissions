# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        intuition, we can try a global dfs
        we recursively search for the two values, keeping track of the common ancestor
        how do we keep track of the common ancestor?
        at each step, as we find the nodes
        we compare the two values with the current node value
        if one of them is smaller and one of them is bigger, then this is 100% the common ancestor as they are on different branches so we return it
        if both of them aare smaller/bigger, 
        best case is we find them split at one small one big between a node
        however could also be like a vertical line where one is below the other (i.e. one node is found first)
        then we return the node.val that is found first 
        this is O(n) space
        however, we notice that we are only ever walking down in one direction, and aren't going back, so there is no need for backtracking at all
        """

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


             