# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head
        prev = None
        node = []
        
        if not head:
            return None
            
        
        while first != None and second != None and second.next:
            
            prev = first
            first = first.next
            second = second.next.next
        
        if prev != None:
            prev.next = prev.next.next
            return head
    
            
        