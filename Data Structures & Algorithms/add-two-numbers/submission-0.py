# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while p1 or p2 or carry:
            sum = carry;
            if p1 is not None:
                sum += p1.val
                p1 = p1.next
            if p2 is not None:
                sum += p2.val
                p2 = p2.next
               

            valu = sum%10
            carry = sum//10
            curr.next = ListNode(valu)

            
            
            curr = curr.next
        return dummy.next
            

        