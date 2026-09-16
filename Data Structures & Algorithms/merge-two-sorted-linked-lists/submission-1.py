# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        for each linked list, the pointer will move forward for the smaller value (default to left if its the same value). 
        so for 1 2 4 and 1 3 5
        1 1 2 3 4 5
        O(n) time 
        if one list is empty, we just return the other one
        if both lists are empty we return empty by default
        """

        if list1 is None: return list2
        if list2 is None: return list1

        head = ListNode(None, None)
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        curr = head

        #non-empty list, iterate down to append smallest element with each step
        while list1 != None or list2 != None:
            if list1 == None:
                print("entered")
                curr.next = list2
                return head
            elif list2 == None:
                curr.next = list1
                return head

            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        return head
