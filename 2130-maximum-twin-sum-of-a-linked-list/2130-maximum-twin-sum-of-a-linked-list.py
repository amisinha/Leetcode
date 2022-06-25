# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values =[]
        tot = []
        
        while head:
            values.append(head.val)
            head = head.next
        l = len(values)
          
        for i in range(0, int(len(values)/2)):
            tot.append(values[i] + values[l-1-i] )
        
        return max(tot)
            
        