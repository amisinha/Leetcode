# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        tot =0
        sumList = []
        curr = dummy = ListNode(0)
       
         
        while head:
            newList.append(head.val)
            head = head.next
        
        for i in range(1,len(newList)):
            if newList[i] != 0:
                tot = tot + newList[i]
            else:
                sumList.append(tot)
                tot = 0
        for i in sumList:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        
      
                
        
       
            
        
                
            
            
        
        