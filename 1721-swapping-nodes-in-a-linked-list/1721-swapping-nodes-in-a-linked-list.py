# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newList = []
        newLL = None
        
        while head is not None:
            newList.append(head.val)
            head = head.next
        
        firstK = newList[k-1]
        l = len(newList)
        lastK = newList[l-k]
        
        newList[k-1] = lastK
        newList[l-k] = firstK
        
        newList.reverse()
        
        for i in newList:
            newLL = ListNode(i, newLL)
        return newLL
        
        
        
        
        
        