# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        kth smallest. bottom-up solution -> in order traversal. O(n) time with O(n) space
        however, this means after node is found, we have to resolve the remaining call stack. 
        should use iterative to end right after
        """

        stack = []
        curr = root
        position = 1

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if position == k:
                return curr.val
            position += 1

            curr = curr.right

