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

        if not p and not q: return True
        if not p or not q: return False

        curr_p = p
        curr_q = q

        stack_p = deque([p])
        stack_q = deque([q])

        while stack_p and stack_q:
            level_size_p = len(stack_p)
            level_size_q = len(stack_q)

            if level_size_p != level_size_q: return False   
            for _ in range (level_size_p):
                curr_p = stack_p.popleft()
                curr_q = stack_q.popleft()

                #handle one of the current Nodes being None
                if not curr_p and curr_q or not curr_q and curr_p: 
                    return False

                #compare left  and rightnodes
                if curr_p and curr_q:
                    if curr_p.val != curr_q.val: return False
                    stack_p.append(curr_p.left)
                    stack_p.append(curr_p.right)

                    stack_q.append(curr_q.left)
                    stack_q.append(curr_q.right)
                    if curr_p.left and curr_q.left:
                        if curr_p.left.val != curr_q.left.val: 
                            return False
                    if not curr_p.left and curr_q.left or curr_p.left and not curr_q.left: 
                        return False

                    if curr_p.right and curr_q.right:
                        if curr_p.right.val != curr_q.right.val: 
                            return False
                    if not curr_p.right and curr_q.right or curr_p.right and not curr_q.right: 
                        return False

        return True
                

                    

            
            



