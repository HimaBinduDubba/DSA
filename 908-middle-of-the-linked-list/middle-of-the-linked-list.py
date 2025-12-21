# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        current=head
        total=0
        while current:
            current=current.next
            total=total+1
        mid=total//2
        current=head
        for _ in range(mid):
            current=current.next
        return current                
        