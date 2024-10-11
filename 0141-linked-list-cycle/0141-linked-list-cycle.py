# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        set_ = {head} 
        if not head:
            return False
        ptr = head.next
        while ptr:
            if ptr.next in set_:
                print(ptr.val)
                return True
            set_.add(ptr)
            ptr = ptr.next
        
        return False
        