# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict ={}
        curr = head
        while curr:
            if curr.val not in dict:
                dict[curr.val] =1
            else:
                dict[curr.val] += 1
            curr = curr.next
        dummy = curr = ListNode()
        
        for key in dict:
            if dict[key] ==1:
                curr.next = ListNode(key)
                curr = curr.next
        return dummy.next
                

        