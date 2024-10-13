# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

            ptr_1 = list1
            ptr_2 = list2
            dummy = ListNode()
            new_list = dummy

            while ptr_1 and ptr_2:
                if ptr_1.val <= ptr_2.val:
                    new_list.next = ptr_1
                    ptr_1 = ptr_1.next
                else:
                    new_list.next = ptr_2
                    ptr_2 = ptr_2.next
                new_list = new_list.next 

            if ptr_1:
                new_list.next = ptr_1
            elif ptr_2:
                new_list.next = ptr_2
            
            return dummy.next
        if len(lists) == 0:
            return 
        res = lists[0]
        for k in range(0,len(lists)-1):
            ptr_2 = lists[k+1]
            res = mergeTwoLists(res, ptr_2)

        return res

        