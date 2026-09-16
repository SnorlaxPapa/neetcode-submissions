# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        to remove the nth node from the end of the list, 
        intuitively we can set up a prev pointer, iterate to the end, alter the pointers, then iterate back
        while this is O(n) time it is O(n) space
        Ideally we want to achieve a O(1) space approach
        We can do one pass through first to find the length of the list and calculate its index k from the front which is length - n
        On the second pass through, we alter the .next pointers for the k - 1 pointer

        Edge cases:
        length == 1, n <= sz so we return None
        k - 1 == -1 (0th index), set the k+1 node as head and return that
        k + 1 == length (last index), set k-1 node as None. actually this edge case would be covered as k - 1 pointer is set as k-1.next.next
        """

        length = 0
        curr = head
        while curr != None:
            length+=1
            curr = curr.next

        if length == 1: return None

        forward_pos = length - n
        if forward_pos == 0: return head.next

        ix = 0
        curr = head
        while ix < forward_pos - 1:
            curr = curr.next
            ix += 1
        
        curr.next = curr.next.next

        return head

        
