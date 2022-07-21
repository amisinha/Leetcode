# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newList = []
        tempList = ListNode()
        cnt = 1
        res = None
        while head is not None:
            newList.append(head.val)
            head = head.next
        newList.reverse()
        
        newList = newList[:n-1] + newList[n:]

        for i in newList:
            res = ListNode(i, res)
        return res
        
        
        
        
        