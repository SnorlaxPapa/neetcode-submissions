# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """intuitive solution:
        we pre-order traverse the tree.
        if the value matches, we run a check to see if the subtrees are identical
        worst case this would be O(m*n) if all the values are equivalent to the root value
        """

        def same_tree(root1, subRoot):
            if not subRoot and not root1: return True

            if subRoot and root1 and subRoot.val == root1.val:
                return same_tree(root1.left, subRoot.left) and same_tree(root1.right, subRoot.right)
            
            else: return False

        if root == None: return False

        if root.val == subRoot.val:
            same = same_tree(root, subRoot)
            if same: return True
            
        left = self.isSubtree(root.left, subRoot)
        if left: return True

        right = self.isSubtree(root.right, subRoot)
        if right: return True

        return False