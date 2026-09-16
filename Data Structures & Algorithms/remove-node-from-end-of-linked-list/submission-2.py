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

        can we do it in one pass? 
        we look at 1, 2, 3, 4
        if we have a fast and slow pointer, we can have the fast pointer be n steps ahead of the slow one
        then, when the fast pointer reaches the end, the slow pointer will be n steps behind
        e.g. for head = [1,2,3,4], n = 2
        fast pointer set to be at 3, slow at 0
        then we increment both while fast.next != None
        once fast hits 4, slow will be at 2. then we can simply set slow.next = slow.next.next and return the head

        edge cases:
        when head.next is None, we just return None
        when n is the size of the array, (i.e. first element being removed), fast pointer will be None. In this case return head.next
        when n is the end of the array (i.e. n = 1), fast pointer will increment to end, slow will be behind that, slow pointer will point to None in slow.next.next = fast.next, alls g
        """

        #handle edge cases
        if head.next == None:
            return None
        
        #declaring s f pointers
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if fast == None: return head.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head


        
