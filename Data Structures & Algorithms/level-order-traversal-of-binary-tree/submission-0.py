# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        queue = deque([root])
        answer = []

        while queue:
            level_size = len(queue)
            temp = []

            for _ in range (level_size):
                curr = queue.popleft()
                if curr: temp.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            answer.append(temp)

        return answer
        