# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given two non-empty linked lists of a reversed number
        each element single digit integer 0 <= i <=9
        I need to add these two numbers together and find the reversed number
        
        to not mutate the original list, i will create a new linked list 

        Intuitive solution: I can read the number from the two lists first O(max(m, n)), 
        solve for the sum, then reverse it by modulo 10 O(max(m, n))

        this solution will take O(max(m, n)) time and O(1) space

        I can speed this process up by iterating down both lists at the same time and creating 
        the number on the fly, thereby removing the need to do a second iteration to create the reversed sum

        So I can have a 
        curr1 and curr2 pointer for l1 l2. we have a carry var to track carried sums
        As we increment curr1 and curr2,
        We calculate curr1.val + curr2.val
        We add our current carry to this sum and reset carry
        We add sum//10 to the carry set sum%10 as the value

        if either one of them hits None, we just iterate down the other list
        """

        curr1 = l1
        curr2 = l2
        head = ListNode()
        curr_new = head
        carry = 0
        while curr1 != None or curr2 != None:
            #handle when curr1/curr2 reaches end before the other
            #we also need to handle the carry if its like carry 1 9 9 9 9 
            if curr1 == None or curr2 == None:
                increment_curr = curr2 if curr1 == None else curr1
                while increment_curr != None:
                    sum_list = increment_curr.val + carry
                    carry = sum_list // 10
                    curr_new.val = sum_list % 10

                    if increment_curr.next != None: curr_new.next = ListNode()
                    else: 
                        curr_new.next = None
                        break

                    increment_curr = increment_curr.next
                    curr_new = curr_new.next
                break
                #handle normal cases
            else:
                sum_list = curr2.val + curr1.val + carry
                curr_new.val = sum_list % 10
                carry = sum_list // 10

                curr1 = curr1.next
                curr2 = curr2.next
                if curr1 == None and curr2 == None: curr_new.next = None
                else:
                    curr_new.next = ListNode()
                    curr_new = curr_new.next

        
        #handle leftover carry
        if carry > 0:
            curr_new.next = ListNode(val=carry, next=None)

        curr = head

        return head

                
                