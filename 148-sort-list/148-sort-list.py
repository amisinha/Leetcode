# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        if head:
            temp = head
            while temp:
                newList.append(temp.val)
                temp = temp.next
            newList.sort()
            finalList = head       
            for i in newList:
                finalList.val = i
                finalList = finalList.next
            return head
            
        