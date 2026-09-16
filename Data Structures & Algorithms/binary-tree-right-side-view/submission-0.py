# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        greatest priority is right side -> then we look left for any deeper nodes -> then we go up a node

        traversal with global depth tracking
        right -> left 
        first we recurse as right as we can with right side view 
        then we recurse left down, appending any nodes that are deeper than the right side 
        we use a nonlocal variable to track the current depth, any left side variables with depth > curr depth is added to the right side view (i.e. they are viewable from the right)
        O(n) space and time
        """

        max_depth = -1
        answer = []

        def dfs(node, curr_depth):
            nonlocal max_depth

            if node == None: return

            if curr_depth > max_depth:
                answer.append(node.val)
                max_depth = curr_depth

            dfs(node.right, curr_depth + 1)
            dfs(node.left, curr_depth + 1)

        dfs(root, 0)

        return answer