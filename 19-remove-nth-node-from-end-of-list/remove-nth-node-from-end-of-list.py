# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        current=head
        while current:
            current=current.next
            k=k+1
        if k-n==0:
            return head.next   
        current=head
        for _ in range(1,k-n):
            current=current.next     
        current.next=current.next.next
        return head    


        