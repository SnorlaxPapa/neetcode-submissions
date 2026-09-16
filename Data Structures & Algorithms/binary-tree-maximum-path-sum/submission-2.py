# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        intuitive solution:
        we need to find the path with the maximum sum in a given tree
        intuitively, we can visit every node in a dfs manner (since we have to visit all the nodes inorder)
        while we visit the nodes, we can keep track of a rolling sum
        if the sum becomes < 0, we reset the sum to 0, this should return the maximum path
        the question is how can we maintain the sum accurately during traversion? 
        we cant just do left_sum = maxpathsum left and right_sum = maxpathsum right because the path may not connect back to the root

        instead we have two possible options during path traversal:
        1) combine left node and right sums. this is the sum of this subtree kind of
        2) left -> up or right -> up, we continue the path up

        so this is actually a post order traversal
        this would be O(n) time with O(n) space in call stack
        """
        
        max_sum = float("-inf")
        def dfs(node):
            if node is None: return 0
            nonlocal max_sum

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            left_sum = left_sum if left_sum > 0 else 0
            right_sum = right_sum if right_sum > 0 else 0

            max_sum = max(max_sum, left_sum + right_sum + node.val)

            return max(left_sum + node.val, right_sum + node.val)

        dfs(root)
        return max_sum
