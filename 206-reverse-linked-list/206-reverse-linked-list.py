# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = head
        dummy2 = head
        values = []
        
        while dummy1:
            values.append(dummy1.val)
            dummy1 = dummy1.next
        
        while dummy2:
            dummy2.val = values.pop()
            dummy2 = dummy2.next
        
        return head
        
        
  
            
        