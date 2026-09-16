# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def conquer(self, l1, l2):
        dummy = ListNode(0, None)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next


    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        middle = l + (r-l)//2
        left = self.divide(lists, l, middle)
        right = self.divide(lists, middle + 1, r)

        return self.conquer(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        intuitive solution
        variable k
        i have a list of all the heads.
        i iterate through lists curr val, find min value (0 if None), then create a new linked node with that val
        if i have k lists and n total elements, that'll be O(kn) run time with O(1) space
        Is there any way to decrease this?

        I know each list is given in ascending order so we can iamge each list as an already merged list waiting to be combined with k - 1 other lists
        so ->
        we have k separate lists
        ok let's think of them as lists for now for ease of ref

        we recursively split k into 2 until we have each individual list, merge each list, then roll back until we get our merged list
        this will be O(logk) in space, O(nlogk) in time

        however, we are constrained to O(1) space, so we cannot recursively split k 
        nvm to hell with the O(1) constraint the optimal solution doesnt even use it
        """
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)
