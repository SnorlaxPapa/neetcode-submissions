# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        we are given integer k to denote how many nodes we need to reverse
        so we must reverse the first k nodes, then reverse the next k nodes, and so on until there are fewer than k nodes left

        intuitive solution:
        we set a prev pointer, for each window k we just reverse to prev 
        so 1 2 3 .next -> .prev

        this would be O(n) runtime with O(n) space

        Is there a way to solve it in O(1) space

        to simplify, suppose we start from n == k
        we have a LL
        1 2 3 

        we start from the start, 
        set 
        prev = None
        curr

        while curr not equals to end of sliding window:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt


        so we save prev, curr, and next per step
        each step, we set the current pointer to be the next nodes pointer

        won't work if k = 1 or k = 2 

        additional condition being If there are fewer than k nodes left, leave the nodes as they are.
        so we can use a 'sliding window' to do an on-the-fly check where we check that it does not become None

        now we need to stitch these individually reversed lists back together. 
        for each reversed list, the last node becomes the new local head, the first node becomes the new local tail
        so for each list, we must connect the new head with the previous tail
        edge case: if k = 1 we can just return the list
        """
        
        if k == 1: return head

        dummy_head = ListNode(0, None)
        previous_tail = dummy_head
        new_list = dummy_head

        count = 1
        curr = head

        while curr != None:
            #we check if this current window segment is valid
            window_end = curr
            while count != k:
                window_end = window_end.next
                if window_end == None: 
                    previous_tail.next = curr
                    return dummy_head.next
                count += 1

            count = 1
            nxt_window_start = window_end.next

            #once valid we reverse starting from curr
            window_start = curr
            prev = None
            while curr != nxt_window_start:
                nxt = curr.next
                curr.next = prev
                
                prev = curr
                curr = nxt

            #now that we are at the window_end (e.g. 1 2 3 -> 3 2 1), we need to stitch it to the previous_tail
            previous_tail.next = prev
            previous_tail = window_start

        return dummy_head.next


