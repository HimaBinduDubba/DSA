# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current=head
        arr=[]
        while current:
            arr.append(current.val)
            current=current.next
        s=''.join(str(a) for a in arr)
        return int(s,2)    

        