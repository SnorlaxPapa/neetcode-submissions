# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        we need a max diameter tracker
        at each step we need to make a choice between two options
            1) we take the left path + right path. this means this cannot go up
            2) we take the max(left, right) and traverse up. this way, we will only travel up and not down as we cannot revisit the same node
        so our max diameter tracker at each step will track 1)
        and we will return 2)
        """
        max_diam = -1

        def dfs(node):
            nonlocal max_diam
            if node == None: return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            if left_path == 0 or right_path == 0: local_path_length = 0
            else: local_path_length = left_path + right_path 

            max_diam = max(max_diam, local_path_length)
            print(node.val, left_path, right_path, max_diam)
            return max(left_path, right_path) + 1
        
        root_path = dfs(root) - 1
        return max(max_diam, root_path)


