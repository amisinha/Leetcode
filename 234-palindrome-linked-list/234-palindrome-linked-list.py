# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy1 = head
        dummy2 = head
        values =[]
        comp1 =[]
        comp2 =[]
        
        
        while dummy1:
            values.append(dummy1.val)
            comp1.append(dummy1.val)
            dummy1 = dummy1.next
        
        while dummy2:
            dummy2.val = values.pop()
            dummy2 = dummy2.next
        
        while head:
            comp2.append(head.val)
            head = head.next
        
        if comp1 == comp2:
            return True
        else:
            return False
            
            
            
        
        
        
        
        
        
        