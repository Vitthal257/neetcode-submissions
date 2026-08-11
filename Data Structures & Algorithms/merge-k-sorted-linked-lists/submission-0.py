# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for ll in lists:
            while ll:
                vals.append(ll.val)
                ll = ll.next
        vals.sort()
        dummy = ListNode(0)
        curr = dummy
        for i in vals:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next

        