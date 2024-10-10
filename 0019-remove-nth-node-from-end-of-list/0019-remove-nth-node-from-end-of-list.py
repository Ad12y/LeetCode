
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = 0
        ptr = head
        while ptr:
            t += 1
            ptr = ptr.next

        if t == 1:
            return None

        d = t - n
        i = 0
        ptr=head
        while i < d-1:
            ptr = ptr.next
            i += 1 
        if i == d:
            return head.next
        ptr.next = ptr.next.next 

        return head
        

        