# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #property of a binary tree, everything on the left must be smaller, everything on the right must be bigger
        if not root: return TreeNode(val=val)

        def dfs(node):
            if val > node.val:
                if not node.right: 
                    node.right = TreeNode(val=val) 
                    return
                dfs(node.right)
            else:
                if not node.left: 
                    node.left = TreeNode(val=val)
                    return
                dfs(node.left)

        dfs(root)
        return root