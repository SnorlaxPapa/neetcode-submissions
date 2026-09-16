# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        intuitively can have a set that marks all the seen list nodes and then we do a O(1) lookup. would be O(n) space and time though
        Questions require O(1) space 
        qn states that the cycle starts frm the tail back to a previous index, so we don't need to worry about cycles starting in between
        we can just find a way to mark each node as seen.
        constraints state node.val is an integer within inclusive range -1000 to 1000
        just mark as None
        """

        if head == None: return False
        
        curr = head
        curr.val = None
        i = 0
        while curr.next != None:
            curr.val = None
            if curr.next.val == None: return True
            curr = curr.next
        
        return False



