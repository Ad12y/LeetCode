# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p_1 = l1
        p_2 = l2
        dummy = ListNode()
        sum_ = dummy
        carry = 0
        while p_1 and p_2:
            if carry:
                t = p_1.val + p_2.val + carry
            else:
                t = p_1.val + p_2.val
            carry = int(t/10)
            if carry:
                t = t%10

            sum_.next = ListNode(t)
            sum_ = sum_.next 
            p_1 = p_1.next
            p_2 = p_2.next
        

        while p_1:
            t = p_1.val + carry
            carry = int(t/10)  
            sum_.next = ListNode(t%10)
            sum_ = sum_.next
            p_1 = p_1.next 

        while p_2:
            t = p_2.val + carry
            carry = int(t/10)
            sum_.next = ListNode(t%10)
            sum_ = sum_.next 
            p_2 = p_2.next
        if carry:
            sum_.next = ListNode(carry)

        return dummy.next
            

        