# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        """
        given a list, we have to re order the list 
        into index [0, n-1, 1, n-2, 2, n-3, ...]

        intuitive solution: create two lists one front one back and append to each other

        cannot reorder values, so must directly manipulate the next pointer
        O(1) constant space in O(n) time
        we can use two pointers
        one pointers will point at the back, one pointer will point at the front
        while the left pointer != right pointer,
        start with left, we set next to be right, then set current right to be left and so on
        so for [0, 1, 2, 3, 4, 5, 6]
        0.next = 6, left pointer increment, 6.next = 1, right pointerr increment, 1.next -> 5, 5.next -> 2 -> 2.next -> 4 -> 4.next 3 equal break
        i must reorder the nodes themselves
        we need to add a prev attribute for the right pointer to iterate backwards 
        we also need to handle the tail
        e.g. for 2 4 6 8, 
        2 8, 4 8, 4, 6 at 4 .next is marked as 6 == right. loop is broken so we should set .next.next = None when i == length - 2
        """

        left = head
        right = head
        length = 1
        #shift right to the end of the array
        while right.next != None:
            prev = right
            right = right.next
            right.prev = prev
            length += 1

        i = 0
        while left != right:
            #temp for pointer management, i to incremenet step by step instead of two steps at once
            if i%2 == 0:    
                temp = left
                left = left.next
                temp.next = right
            else:
                temp = right
                right = right.prev
                temp.next = left

            if i == length - 2: temp.next.next = None
            i+=1




            