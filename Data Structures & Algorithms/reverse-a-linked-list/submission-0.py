# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """head -> next
        we save head.next, set head.next = None, move to the next saved node, 
        save .next, set next to be curr, then move and repeat"""
        if head == None: return None
        
        nextNode = head.next
        head.next = None
        prev = head

        while nextNode != None:
            curr = nextNode
            nextNode = curr.next
            curr.next = prev 
            prev = curr

        return prev